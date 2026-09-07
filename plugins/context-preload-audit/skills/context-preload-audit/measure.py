#!/usr/bin/env python3
"""Estimate Claude Code preload size from configurable sources. Read-only; never edits config.
Usage: python3 measure.py [--json] [--run-hooks] [--baseline [--reset]] [--verify [--backup DIR]]
  (default)    list SessionStart hook commands WITHOUT executing them (size shown as "not run")
  --run-hooks  execute SessionStart hook commands (shell, stdin closed, 25 s timeout) to measure
               their real output. Only pass this after reading the commands in ~/.claude/settings.json.
  --json       append a JSON object (schema below) after the text report, for CI or diffing
  --baseline   write baseline.json next to this script if absent, else compare and report drift
               (--reset overwrites it)
  --verify     no-regression check of trimmed items against backups in
               ~/.claude/skills_disabled/backup-*/ (or --backup DIR); hook checks need --run-hooks
Requires Python 3.9+, standard library only.
JSON schema: {"rows":[[source,item,chars]...],"total":int,"tok":int,"hooks_executed":bool,
              "plugins":{name:{enabled,agents,skills,chars,key}},"user_skills":{name:chars},
              "extensions":{file:isEnabled},"extension_dir":str|null}
"""
import json, os, re, glob, subprocess, sys
A = sys.argv[1:]
RUN_HOOKS = '--run-hooks' in A
H = os.path.expanduser('~')
SETTINGS = os.path.join(H, '.claude', 'settings.json')
CACHE = os.path.join(H, '.claude', 'plugins', 'cache')
SKILLS = os.path.join(H, '.claude', 'skills')
BACKUP_GLOB = os.path.join(H, '.claude', 'skills_disabled', 'backup-*')

# desktop-extension settings dir: first existing candidate wins; absent dir is fine
_EXT_CANDIDATES = [
    os.path.join(H, 'Library', 'Application Support', 'Claude', 'Claude Extensions Settings'),          # macOS
    os.path.join(os.environ.get('APPDATA', os.path.join(H, 'AppData', 'Roaming')), 'Claude', 'Claude Extensions Settings'),  # Windows
    os.path.join(os.environ.get('XDG_CONFIG_HOME', os.path.join(H, '.config')), 'Claude', 'Claude Extensions Settings'),     # Linux
]
EXT_DIR = next((p for p in _EXT_CANDIDATES if os.path.isdir(p)), None)

S = {}
if os.path.exists(SETTINGS):
    try: S = json.load(open(SETTINGS))
    except Exception as e: print(f'warn: cannot parse {SETTINGS}: {e}; treating as empty', file=sys.stderr)
if not isinstance(S, dict): S = {}

def fm(path):
    """Parse simple YAML frontmatter (key: value, folded continuation lines)."""
    try: t = open(path, errors='ignore').read()
    except OSError: return {}
    m = re.match(r'---\r?\n(.*?)\r?\n---', t, re.S)
    if not m: return {}
    d, cur = {}, None
    for line in m.group(1).split('\n'):
        mm = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
        if mm: cur = mm.group(1); d[cur] = mm.group(2)
        elif cur: d[cur] += '\n' + line
    return d

def hook_cmds():
    hs = S.get('hooks', {}) if isinstance(S.get('hooks'), dict) else {}
    for h in hs.get('SessionStart', []) or []:
        for c in (h.get('hooks', []) or []) if isinstance(h, dict) else []:
            if isinstance(c, dict) and c.get('command'): yield c['command']

def run_hook(cmd):
    """Execute a hook command exactly as Claude Code would (shell). Only called with --run-hooks."""
    return subprocess.run(cmd, shell=True, capture_output=True, text=True,
                          stdin=subprocess.DEVNULL, timeout=25).stdout

rows = []      # (source, item, chars)
def add(src, item, chars): rows.append((src, item, chars))

# 1. enabled plugins: agents + skills + commands
plugins = {}
ep = S.get('enabledPlugins', {}) if isinstance(S.get('enabledPlugins'), dict) else {}
for k, v in ep.items():
    name, _, market = k.partition('@')
    dirs = glob.glob(os.path.join(CACHE, market or '*', name, '*'))
    ag = sk = 0; nag = nsk = 0
    for b in dirs:
        for a in glob.glob(os.path.join(b, 'agents', '*.md')):
            d = fm(a); ag += len(name) + len(os.path.basename(a)) + len(d.get('description', '')) + len(d.get('tools', '')) + 30; nag += 1
        for s in glob.glob(os.path.join(b, 'skills', '*', 'SKILL.md')) + glob.glob(os.path.join(b, 'commands', '*.md')):
            d = fm(s); sk += len(name) + len(d.get('name', os.path.basename(os.path.dirname(s)))) + len(d.get('description', '')) + 10; nsk += 1
    plugins[name] = dict(enabled=bool(v), agents=nag, skills=nsk, chars=ag + sk, key=k)
    if v:
        add('plugin', f'{name} ({nag} agents, {nsk} skills/cmds)', ag + sk)

# 2. user skills
user_skills = {}
for s in glob.glob(os.path.join(SKILLS, '*', 'SKILL.md')):
    d = fm(s); n = d.get('name', os.path.basename(os.path.dirname(s)))
    c = len(n) + len(d.get('description', '')) + 10
    user_skills[n] = c; add('user-skill', n, c)

# 3. SessionStart hooks (not executed unless --run-hooks)
hooks_listed = 0
for cmd in hook_cmds():
    hooks_listed += 1
    label = cmd[:60].replace('\n', ' ')
    if not RUN_HOOKS:
        add('SessionStart-hook', label + '  [not run]', 0); continue
    try: out = run_hook(cmd)
    except subprocess.TimeoutExpired: out = ''; label += '  [TIMEOUT]'
    except OSError as e: out = ''; label += f'  [ERROR {e.__class__.__name__}]'
    try: out = json.loads(out)['hookSpecificOutput']['additionalContext']
    except Exception: pass
    add('SessionStart-hook', label, len(out))

# 4. desktop extensions
exts = {}
if EXT_DIR:
    for f in glob.glob(os.path.join(EXT_DIR, '*.json')):
        try: j = json.load(open(f))
        except Exception: continue
        en = bool(j.get('isEnabled', True)) if isinstance(j, dict) else True
        exts[os.path.basename(f)] = en
        if en: add('desktop-extension', os.path.basename(f), 0)   # tool names deferred; per-tool cost unknown here

# ---- report
tot = sum(c for _, _, c in rows)
print(f'{"SOURCE":20s} {"ITEM":50s} {"chars":>7s} {"~tok":>6s}')
for src, item, c in sorted(rows, key=lambda r: -r[2]):
    print(f'{src:20s} {item[:50]:50s} {c:7d} {c//4:6d}')
print(f'{"TOTAL configurable":71s} {tot:7d} {tot//4:6d}')
if hooks_listed and not RUN_HOOKS:
    print(f'\nNOTE: {hooks_listed} SessionStart hook command(s) listed but NOT executed, so their size is 0 above.\n'
          f'      Read them in {SETTINGS} (hooks.SessionStart); if you trust them, re-run with --run-hooks.')
if not S: print(f'\nNOTE: no readable {SETTINGS}; plugins and hooks not measured.')
if EXT_DIR is None: print('\nNOTE: no desktop-extension settings dir found (looked for: ' + '; '.join(_EXT_CANDIDATES) + ')')

# ---- candidates
print('\nCANDIDATES (largest first; propose only, this script never applies anything):')
cands = []
for name, p in plugins.items():
    if p['enabled'] and p['chars'] > 800:
        cands.append((p['chars'], f'plugin {name}: {p["agents"]} agents/{p["skills"]} skills -> set "{p["key"]}": false in {SETTINGS}'))
for n, c in user_skills.items():
    if c > 450:
        cands.append((c, f'user skill {n}: description {c} chars -> shorten to one sentence in {os.path.join(SKILLS, n, "SKILL.md")}'))
for src, item, c in rows:
    if src == 'SessionStart-hook' and c > 400:
        cands.append((c, f'SessionStart hook output {c} chars -> trim command in {SETTINGS} hooks.SessionStart'))
if rows:   # always surface the single largest item so the top cost is never hidden by thresholds
    src, item, c = max(rows, key=lambda r: r[2])
    if c and not any(cc == c for cc, _ in cands):
        cands.append((c, f'LARGEST item is {src} {item} ({c} chars); below trim threshold, review manually'))
pl_skill_names = set()   # duplicates: user skill names colliding with plugin skill names
for k, v in ep.items():
    if not v: continue
    name = k.split('@')[0]
    for b in glob.glob(os.path.join(CACHE, '*', name, '*')):
        for s in glob.glob(os.path.join(b, 'skills', '*', 'SKILL.md')):
            pl_skill_names.add(fm(s).get('name', os.path.basename(os.path.dirname(s))))
for n in user_skills:
    if n in pl_skill_names:
        cands.append((100, f'DUPLICATE: user skill "{n}" also provided by an enabled plugin -> move {os.path.join(SKILLS, n)} out of the skills dir'))
for e, en in exts.items():   # duplicates: desktop extension vs plugin (e.g. pdf-server-mcp vs pdf-viewer plugin)
    if en and 'pdf' in e and plugins.get('pdf-viewer', {}).get('enabled'):
        cands.append((400, f'DUPLICATE: desktop extension {e} overlaps plugin pdf-viewer -> set "isEnabled": false in {os.path.join(EXT_DIR, e)}'))
for c, msg in sorted(cands, reverse=True):
    print(f'  ~{c//4:5d} tok  {msg}')
if not cands: print('  none above thresholds')
print('\nNOT MEASURABLE HERE: claude.ai connectors (claude.ai > Settings > Connectors), MCP server instructions, built-in tool list, desktop-extension tool names.')
if '--json' in A:
    print(json.dumps(dict(rows=rows, total=tot, tok=tot // 4, hooks_executed=RUN_HOOKS, plugins=plugins,
                          user_skills=user_skills, extensions=exts, extension_dir=EXT_DIR), indent=1))

# ---- baseline / drift
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'baseline.json')
if '--baseline' in A:
    import datetime
    cur = dict(date=str(datetime.date.today()), total=tot, tok=tot // 4, hooks_executed=RUN_HOOKS,
               rows={f'{s}:{i}': c for s, i, c in rows})
    if os.path.exists(BASE):
        b = json.load(open(BASE))
        d = tot - b['total']; pct = 100.0 * d / max(b['total'], 1)
        print(f"\nBASELINE {b['date']}: {b['total']} chars / ~{b['tok']} tok; now {tot} / ~{tot//4} ({d:+d} chars, {pct:+.1f}%)")
        if b.get('hooks_executed') != RUN_HOOKS: print('  note: baseline and this run differ in --run-hooks; hook rows are not comparable')
        if pct > 10: print('  DRIFT > 10%: something new is preloaded; re-run the procedure')
        for k, c in cur['rows'].items():
            if k not in b['rows']: print(f'  new: {k} {c}')
        for k in b['rows']:
            if k not in cur['rows']: print(f'  gone: {k}')
        if '--reset' in A: json.dump(cur, open(BASE, 'w'), indent=1); print('  baseline reset')
    else:
        json.dump(cur, open(BASE, 'w'), indent=1); print(f'\nBASELINE written: {BASE} ({tot} chars / ~{tot//4} tok)')

# ---- verify: no-regression check against backups (never fails silently, never edits)
if '--verify' in A:
    fails = 0
    def ok(m): print('  ok   ' + m)
    def bad(m):
        global fails; fails += 1; print('  FAIL ' + m)
    def body(path):  # everything after frontmatter
        s = open(path, errors='ignore').read(); m = re.match(r'---\r?\n.*?\r?\n---\r?\n?', s, re.S)
        return s[m.end():] if m else s
    print('\nVERIFY (functionality preservation):')
    if '--backup' in A:
        try: bdirs = [A[A.index('--backup') + 1]]
        except IndexError: print('  FAIL --backup needs a directory argument'); sys.exit(2)
    else:
        bdirs = sorted(glob.glob(BACKUP_GLOB))
    if not bdirs:
        print(f'  FAIL no backup directory found (looked for: {BACKUP_GLOB}; or pass --backup DIR)')
        print('       expected layout: <dir>/hook-output*.txt, <dir>/<skill>.SKILL.md or <dir>/<skill>/SKILL.md')
        sys.exit(1)
    print(f'  info backup dirs: {bdirs}')
    # 1. hook output: valid JSON, real newlines, field set unchanged vs backup snapshot
    hooks_out = []
    cmds = list(hook_cmds())
    if cmds and not RUN_HOOKS:
        print(f'  skip hook checks ({len(cmds)} command(s)): not executed without --run-hooks')
    for cmd in cmds if RUN_HOOKS else []:
        try: raw = run_hook(cmd)
        except subprocess.TimeoutExpired: bad(f'hook timed out: {cmd[:50]}'); continue
        except OSError as e: bad(f'hook could not run ({e.__class__.__name__}): {cmd[:50]}'); continue
        try: ctx = json.loads(raw)['hookSpecificOutput']['additionalContext']
        except Exception: bad(f'hook output is not valid hook JSON: {cmd[:50]}'); continue
        ok('hook output is valid JSON')
        if '\\n' in ctx and '\n' not in ctx: bad('hook context has literal \\n instead of real newlines')
        else: ok('hook context uses real newlines')
        hooks_out.append(ctx)
    fields = lambda s: set(re.findall(r'\b([a-z_][a-z0-9_]*)(?==|:(?:\s|$))', s, re.M))
    snaps = [f for d in bdirs for f in glob.glob(os.path.join(d, 'hook-output*.txt'))]
    if hooks_out and snaps:
        old = fields(open(snaps[-1]).read()); new = fields('\n'.join(hooks_out))
        miss = old - new
        if miss: bad(f'hook fields missing vs backup snapshot: {sorted(miss)}')
        else: ok(f'hook field set preserved ({len(old)} fields)')
    elif hooks_out:
        print('  info hook: no hook-output*.txt in ' + ', '.join(bdirs) +
              '; save one with: <hook cmd> </dev/null | jq -r .hookSpecificOutput.additionalContext > <backupdir>/hook-output-before.txt')
    # 2. user skills: description non-empty, trigger phrases kept, body unchanged vs backup
    checked = 0
    for s in glob.glob(os.path.join(SKILLS, '*', 'SKILL.md')):
        n = os.path.basename(os.path.dirname(s)); d = fm(s); desc = d.get('description', '').strip()
        if not desc: bad(f'skill {n}: empty description'); continue
        bk = [f for dd in bdirs for f in glob.glob(os.path.join(dd, f'{n}.SKILL.md')) + glob.glob(os.path.join(dd, n, 'SKILL.md'))]
        if not bk: continue
        checked += 1
        ob = fm(bk[-1]).get('description', '')
        norm = lambda x: re.sub(r'\s+', ' ', x).lower()
        trig = [norm(q) for q in re.findall(r'"([^"]{3,60})"', ob) if norm(q) not in norm(desc)]
        if trig: bad(f'skill {n}: trigger phrases dropped: {trig}')
        else: ok(f'skill {n}: trigger phrases kept')
        if body(bk[-1]).strip() == body(s).strip(): ok(f'skill {n}: body identical to backup')
        else: bad(f'skill {n}: body differs from backup (only the description should change)')
    if not checked:
        print('  info skills: no backup matched any skill (looked for <dir>/<skill>.SKILL.md or <dir>/<skill>/SKILL.md in ' + ', '.join(bdirs) + ')')
    # 3. disabled plugins/extensions: list for explicit confirmation
    dis = [k for k, v in ep.items() if not v]
    dex = [e for e, en in exts.items() if not en]
    if dis or dex: print(f'  info disabled (confirm no workflow uses them): plugins={dis} extensions={dex}')
    # 4. diff pointer for every backed-up file
    for d in bdirs:
        for f in glob.glob(os.path.join(d, '*')):
            print(f'  diff {f}  (only labels/prose may differ; no removed data or instructions)')
    if not hooks_out and not checked: print('  note: nothing was compared; PASS below means "no regression detected", not "verified"')
    print(f'VERIFY RESULT: {"PASS" if not fails else f"{fails} FAIL(S) -> revert the trim, do not argue for it"}')
    sys.exit(1 if fails else 0)
