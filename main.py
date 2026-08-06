import json
from typing import Any
import typer
from pathlib import Path
import subprocess
import shutil
import os


# Constants
UTILITY_FOLDER_PATH = Path('./umutils')
CONFIG_FILE_PATH = Path('./umconfig.json')
UTILITY_SERVICES = 'UTILITY_SERVICES'
CONFIGS: dict[str, Any] = {
    UTILITY_SERVICES: []
}


# Function to load the configs
def load_configs():
    if not CONFIG_FILE_PATH.is_file():
        with open(CONFIG_FILE_PATH, 'w') as CONFIG_FILE:
            json.dump(CONFIGS, CONFIG_FILE)

        return CONFIGS

    configs = {}

    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            configs: dict[str, Any] = json.load(f)
    except FileNotFoundError:
        print(f'ERROR: file {CONFIG_FILE_PATH} does not exists')
    except Exception as e:
        print(f'ERROR: {e}')
        exit(1)

    return configs


# Function to save the configs
def update_configs():
    try:
        with open(CONFIG_FILE_PATH, 'w') as f:
            json.dump(CONFIGS, f)
    except Exception as e:
        raise e


CONFIGS = load_configs()

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
def add(path: str):
    """Add a new utility service

    Args:
        path (str): The path of the utility service to add.
    """
    if not path.endswith('.exe'):
        path = f'{path}.exe'

    shutil.copy(path, UTILITY_FOLDER_PATH)
    CONFIGS[UTILITY_SERVICES].append(path[:-4])
    update_configs()
    print(f'Service "{path[:-4]}" added successfully.')


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
        os.remove(UTILITY_FOLDER_PATH / f'{name}.exe')
        CONFIGS[UTILITY_SERVICES].remove(name)
        update_configs()
        print(f'Service "{name}" removed successfully.')
    except FileNotFoundError:
        print(f'Service "{name}" not found, possible cause - UTILITY FOLDER Tampered.')
    except Exception as e:
        print(f'Service "{name}" not deleted due to following reason -\n{e}')


if __name__ == '__main__':
    app()