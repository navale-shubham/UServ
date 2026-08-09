import json
import typer
import shutil
from pathlib import Path
from typing import Annotated

from configs import TOOLS_FOLDER_PATH, TOOL_LIST_FILE_PATH


with open(TOOL_LIST_FILE_PATH, 'r') as TOOL_LIST_FILE:
    TOOL_LIST: list[str] = json.load(TOOL_LIST_FILE)


def update_tool_list_file():
    try:
        with open(TOOL_LIST_FILE_PATH, 'w') as TOOL_LIST_FILE:
            json.dump(TOOL_LIST, TOOL_LIST_FILE)
    except Exception as e:
        raise e


app = typer.Typer(rich_markup_mode=None, pretty_exceptions_enable=False)


@app.command()
def list():
    """List available tools"""
    if not TOOL_LIST:
        return

    print('Tools:')
    for s in TOOL_LIST:
        print(f'  {s}')


@app.command()
def add(
    name: Annotated[str, typer.Argument(help="The name of the tool.")],
    path: Annotated[Path, typer.Argument(help="The path of the tool.")]
    ):
    """Add a new tool"""

    if name in TOOL_LIST:
        print(f'Tool with the same name already exists.')
        return

    shutil.copy(path, (TOOLS_FOLDER_PATH / name).with_suffix('.exe'))
    TOOL_LIST.append(name)
    update_tool_list_file()
    print(f'Tool "{name}" added successfully.')


@app.command()
def remove(
    name: Annotated[str, typer.Argument(help="The name of the tool.")]
    ):
    """Remove an existing tool"""

    if name not in TOOL_LIST:
        print(f'Tool "{name}" does not exist.')
        return

    try:
        Path((TOOLS_FOLDER_PATH / name).with_suffix('.exe')).unlink()
        TOOL_LIST.remove(name)
        update_tool_list_file()
        print(f'Tool "{name}" removed successfully.')
    except FileNotFoundError:
        print(f'Tool "{name}" not found, possible cause - UTILITIES FOLDER Tampered.')
    except Exception as e:
        print(f'Tool "{name}" not deleted due to following reason -\n{e}')


if __name__ == '__main__':
    app()