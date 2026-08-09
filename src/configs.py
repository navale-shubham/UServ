from pathlib import Path
import sys
import json


TOOL_LIST_FILE_TEMPLATE: list[str] = []

if getattr(sys, "frozen", False):
    # Packaged application
    APP_DATA = Path(sys.executable).parent
else:
    # Development
    APP_DATA = Path(__file__).resolve().parent.parent / "tests/data"

APP_DATA.mkdir(parents=True, exist_ok=True)

TOOLS_FOLDER_PATH = APP_DATA / 'tools'
TOOLS_FOLDER_PATH.mkdir(parents=True, exist_ok=True)

TOOL_LIST_FILE_PATH = APP_DATA / 'tool_list.json'
if not TOOL_LIST_FILE_PATH.exists():
    TOOL_LIST_FILE_PATH.touch(exist_ok=True)
    with open(TOOL_LIST_FILE_PATH, 'w') as TOOL_LIST_FILE:
        json.dump(TOOL_LIST_FILE_TEMPLATE, TOOL_LIST_FILE)