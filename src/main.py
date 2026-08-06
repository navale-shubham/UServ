import json
from typing import Any
import typer
import subprocess
import shutil
from pathlib import Path

from paths import UTILITY_FOLDER_PATH, CONFIG_FILE_PATH
from configs import CONFIG_TEMPLATE


# Constants
UTILITY_SERVICES = 'UTILITY_SERVICES'

if not CONFIG_FILE_PATH.exists():
    CONFIG_FILE_PATH.touch()
    with open(CONFIG_FILE_PATH, 'w') as CONFIG_FILE:
        json.dump(CONFIG_TEMPLATE, CONFIG_FILE)

with open(CONFIG_FILE_PATH, 'r') as CONFIG_FILE:
    CONFIGS: dict[str, Any] = json.load(CONFIG_FILE)


# Function to save the configs
def update_configs():
    try:
        with open(CONFIG_FILE_PATH, 'w') as f:
            json.dump(CONFIGS, f)
    except Exception as e:
        raise e


app = typer.Typer()

@app.command()
def run(name: str):
    """Run utility services

    Args:
        name (str): The name of the utility process to run.
    """
    if name not in CONFIGS[UTILITY_SERVICES]:
        print(f'Service named "{name}" does not exists.')
        return

    subprocess.run([UTILITY_FOLDER_PATH / name])


@app.command()
def ls():
    """List available utility services"""
    if not CONFIGS[UTILITY_SERVICES]:
        return

    print('Utility Services:')
    for s in CONFIGS[UTILITY_SERVICES]:
        print(f'  {s}')


@app.command()
def add(path: Path):
    """Add a new utility service

    Args:
        path (str): The path of the utility service to add.
    """
    if path.stem in CONFIGS[UTILITY_SERVICES]:
        print(f'Service with name "{path.stem}" already exists.')
        return

    path = path.with_suffix('.exe')

    shutil.copy(path, UTILITY_FOLDER_PATH)
    CONFIGS[UTILITY_SERVICES].append(path.stem)
    update_configs()
    print(f'Service "{path.stem}" added successfully.')


@app.command()
def remove(name):
    """Remove an existing utility service

    Args:
        name (str): The name of the utility service to remove.
    """
    if name not in CONFIGS[UTILITY_SERVICES]:
        print(f'Service "{name}" does not exists.')
        return

    try:
        Path(UTILITY_FOLDER_PATH / f'{name}.exe').unlink()
        CONFIGS[UTILITY_SERVICES].remove(name)
        update_configs()
        print(f'Service "{name}" removed successfully.')
    except FileNotFoundError:
        print(f'Service "{name}" not found, possible cause - UTILITY FOLDER Tampered.')
    except Exception as e:
        print(f'Service "{name}" not deleted due to following reason -\n{e}')


if __name__ == '__main__':
    app()