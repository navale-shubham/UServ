from pathlib import Path
import os
import sys


if getattr(sys, "frozen", False):
    # Packaged application
    APP_DATA = Path(os.environ['LOCALAPPDATA']) / 'Utility Manager'
else:
    # Development
    APP_DATA = Path(__file__).resolve().parent.parent / "tests/data"

APP_DATA.mkdir(parents=True, exist_ok=True)

UTILITY_FOLDER_PATH = APP_DATA / 'utils'
UTILITY_FOLDER_PATH.mkdir(parents=True, exist_ok=True)

CONFIG_FILE_PATH = APP_DATA / 'config.json'