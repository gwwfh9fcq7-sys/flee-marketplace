# Publishing flee

This repo is a Claude plugin **marketplace** named `flee`, containing the `flee`
plugin. Going live means hosting it so `/plugin install` can reach it. Two routes.

## State: ready to push

- Marketplace name: `flee` · Plugin: `flee` · Version: `0.3.0`
- Both manifests pass `claude plugin validate`.
- The only edit left is optional: add a `repository` URL to
  `plugins/flee/.claude-plugin/plugin.json` once your GitHub repo exists.
- Install identifier users will type: `/plugin install flee@flee`. (If you'd rather it
  read `flee@flee-tools`, change the top-level `name` in
  `.claude-plugin/marketplace.json` to `flee-tools`. It cannot be an Anthropic reserved
  name.)

## Route A — your own GitHub marketplace (fastest, full control)

```bash
# from this folder
git init && git add -A && git commit -m "flee 0.3.0"
git branch -M main
git remote add origin https://github.com/<you>/flee-marketplace.git
git push -u origin main
```

Anyone installs with:

```
/plugin marketplace add <you>/flee-marketplace
/plugin install flee@flee
```

The commands then namespace under the brand: `/flee:plan`, `/flee:next`,
`/flee:schedule`, `/flee:review`, `/flee:improve`.

Ship an update by bumping `version` in `plugins/flee/.claude-plugin/plugin.json` and
pushing. Users get it on `/plugin marketplace update`. (Bumping the version is
required — an unchanged version string means existing users see no update.)

## Route B — the community marketplace (public discovery at claude.com/plugins)

Free, but screened. Submit per Anthropic's guide "Submit your plugin to the community
marketplace" (docs.claude.com → Plugins). It runs automated validation + safety
screening and pins your plugin to a commit SHA in
`anthropics/claude-plugins-community`. Once accepted, anyone installs with:

```
/plugin marketplace add anthropics/claude-plugins-community
/plugin install flee@claude-community
```

Route A gets you shareable today; Route B gets you discoverability. They're not
exclusive — publish A now, submit to B when you want reach.

## Two honest caveats

- **Free only.** There is no native way to charge for a plugin; "live" means free
  install. Value is distribution and reputation, not direct revenue.
- **Scheduling portability.** `/flee:schedule` lists the Cowork scheduled-task tools in
  its `allowed-tools`. In other hosts the scheduled-task tool names differ, so reminders
  may not fire there. The rest of the plugin is host-agnostic.
