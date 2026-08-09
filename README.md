# Utility Manager (`um`)

A lightweight, unified CLI utility designed to easily manage and execute custom Windows command-line tools.

---

## Features

- **Centralized Management**: Register custom executables under clean short names.
- **Seamless PATH Integration**: Automatically adds installed utilities to your User `PATH` so they can be run from any terminal session.
- **Simple CLI Commands**:
  - `list`: Show all currently installed custom utilities.
  - `add`: Register a new custom utility.
  - `remove`: Unregister and delete a utility.

---

## Command Reference

### List Installed Utilities
Display all registered utilities:
```bash
um list
```

### Add a Utility
Register an executable script or binary under a custom name:
```bash
um add <tool_name> <path_to_executable>
```
*Example:*
```bash
um add mytool C:\path\to\script.exe
```

### Remove a Utility
Unregister and delete a utility executable:
```bash
um remove <tool_name>
```
*Example:*
```bash
um remove mytool
```

---

## Development & Building

### Project Prerequisites
- Python 3.14 or higher
- `uv` package manager (or standard `pip`)

### Local Setup
1. Clone the repository and navigate to the project directory:
   ```bash
   cd "Utility Manager"
   ```
2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```
3. Run the CLI directly:
   ```bash
   uv run python src/main.py --help
   ```

### Building the Executable
To bundle the application into a standalone Windows binary using PyInstaller:
```bash
uv run pyinstaller um.spec
```
This generates the standalone application directory at `dist/um/`.

### Creating the Setup Installer
Compile the setup wizard using Inno Setup:
1. Open [um.iss](um.iss) in Inno Setup Compiler.
2. Compile the script to generate `dist/Utility Manager Setup.exe`.
3. Running the installer will deploy `um.exe` and configure `{app}` and `{app}\tools` in your user `PATH`.

---

## Project Architecture

```
Utility Manager/
├── assets/             # Icons and visual assets
├── src/
│   ├── configs.py      # Path resolution and environment setup
│   └── main.py         # Typer CLI definition and commands
├── PROJECT_SPEC.md     # Technical specification and architecture details
├── pyproject.toml      # Project dependencies and configuration
├── um.iss              # Inno Setup installation script
└── um.spec             # PyInstaller build specification
```
