# Project Specification: Utility Manager (`um`)

## Problem Statement
Command-line utility scripts and executables often get scattered across different directories on Windows systems. Navigating to specific folders or manually updating system environment variables to execute custom utilities creates friction.

**Utility Manager (`um`)** provides a unified command-line interface (CLI) to register, manage, and remove custom utility executables, automatically integrating them into the system environment for seamless CLI execution.

---

## Core Capabilities & Feature Requirements

### 1. Tool Listing (`um list`)
- Displays all currently registered custom utilities listed in `tool_list.json`.
- Returns clean CLI output listing tool names line-by-line.

### 2. Tool Addition (`um add <name> <path>`)
- Accepts a custom tool identifier (`name`) and source file path (`path`).
- Copies the target executable into the application's central `tools/` storage directory as `<name>.exe`.
- Persists the new utility entry in `tool_list.json`.
- Prevents duplicate tool names from being added.

### 3. Tool Removal (`um remove <name>`)
- Unlinks and removes the corresponding executable file (`tools/<name>.exe`).
- Removes the utility entry from `tool_list.json`.
- Gracefully handles missing files or environment tampering.

---

## Technical Architecture & Design

### Technology Stack
- **Language**: Python >= 3.14
- **CLI Framework**: [Typer](https://typer.tiangolo.com/) (`typer>=0.27.1`)
- **Packaging**: [PyInstaller](https://pyinstaller.org/) (`pyinstaller>=6.22.0`)
- **Installer**: Inno Setup Compiler (`um.iss`)
- **Package & Dependency Manager**: `uv`

### Application Structure
- [src/main.py](src/main.py): Primary CLI application definition and Typer commands (`list`, `add`, `remove`).
- [src/configs.py](src/configs.py): Runtime configuration and storage resolution logic (`APP_DATA`, `TOOLS_FOLDER_PATH`, `TOOL_LIST_FILE_PATH`).

### Runtime Environment Handling
- **Development Mode**: Resolves application data path to `tests/data/`.
- **Packaged Executable Mode**: Detects `sys.frozen` flag and resolves application storage relative to `sys.executable`.

### Installation & Deployment Architecture
- `PyInstaller` bundles [src/main.py](src/main.py) into a standalone executable directory `dist/um/um.exe`.
- Inno Setup (`um.iss`) builds a native Windows Setup executable (`dist/Utility Manager Setup.exe`).
- The installer automatically updates the user's `Path` environment variable in the registry (`HKCU\Environment\Path`) to include:
  - `{app}` (containing `um.exe`)
  - `{app}\tools` (containing installed custom tools)