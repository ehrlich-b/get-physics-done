# GPD Onboarding Hub

This page is the shortest path for a non-coder to get started with GPD.

Use this hub to pick:
- your operating system guide
- your runtime guide

## First: terminal vs runtime

You will use two different places:

- Your **normal terminal** is where you install GPD and check basic tools like Node and Python.
- Your **runtime** is the AI app where you actually use GPD commands after install.

If you only remember one order, use this:
`help -> start -> tour -> new-project / map-research -> resume-work`

`help` shows the command list. `start` helps you choose a path if you are unsure. `tour` is the read-only walkthrough. `new-project`, `map-research`, and `resume-work` are the main next steps after that.

<details>
<summary>Common beginner terms</summary>

- **Runtime**: the AI terminal app you talk to, such as Claude Code, Codex, Gemini CLI, or OpenCode.
- **API credits**: paid model usage from the provider behind your runtime.
- **`--local`**: install GPD for just this project or folder.
- **`gpd resume`**: the terminal-side recovery step.
- **`resume-work`**: the in-runtime command you use after reopening the right workspace.

</details>

## Choose your OS

<details>
<summary>macOS</summary>

Use this if you are on a Mac.

- [macOS guide](./macos.md)

</details>

<details>
<summary>Windows</summary>

Use this if you are on Windows 10 or 11.

- [Windows guide](./windows.md)

</details>

<details>
<summary>Linux</summary>

Use this if you are on Linux.

- [Linux guide](./linux.md)

</details>

## Choose your runtime

<details>
<summary>Claude Code</summary>

Use this if you want GPD inside Claude Code. Inside the runtime, GPD commands use `/gpd:...`.

- Install: `npx -y get-physics-done --claude --local`
- [Claude Code quickstart](./claude-code.md)

</details>

<details>
<summary>Codex</summary>

Use this if you want GPD inside Codex. Inside the runtime, GPD commands use `$gpd-...`.

- Install: `npx -y get-physics-done --codex --local`
- [Codex quickstart](./codex.md)

</details>

<details>
<summary>Gemini CLI</summary>

Use this if you want GPD inside Gemini CLI. Inside the runtime, GPD commands use `/gpd:...`.

- Install: `npx -y get-physics-done --gemini --local`
- [Gemini CLI quickstart](./gemini-cli.md)

</details>

<details>
<summary>OpenCode</summary>

Use this if you want GPD inside OpenCode. Inside the runtime, GPD commands use `/gpd-...`.

- Install: `npx -y get-physics-done --opencode --local`
- [OpenCode quickstart](./opencode.md)

</details>

## How to use the guides

1. Open your OS guide and make sure Node and Python are installed.
2. Open your runtime guide and confirm the runtime starts from the normal terminal.
3. Install GPD with the runtime-specific command in that guide.
4. Inside the runtime, start with `help`, then `start`, then `tour`.
5. After that, choose `new-project`, `map-research`, or `resume-work` depending on your situation.

If you want the most guided path, follow the runtime guide first, then come back here only when you need the next step.
