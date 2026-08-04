import json
import typer
from pathlib import Path
import subprocess


# Constants
UTILITY_FOLDER_PATH = Path('./umutils')
CONFIG_FILE_PATH = Path('./umconfig.json')
UTILITY_SERVICES = 'UTILITY_SERVICES'
CONFIGS = {
    UTILITY_SERVICES: []
}

if not CONFIG_FILE_PATH.is_file():
    with open(CONFIG_FILE_PATH, 'w') as f:
        json.dump(CONFIGS, f)

# Load configurations
try:
    with open(CONFIG_FILE_PATH, 'r') as f:
        CONFIGS = json.load(f)
except FileNotFoundError:
    print(f'ERROR: file {CONFIG_FILE_PATH} does not exists')
except Exception as e:
    print(f'ERROR: {e}')
    exit(1)

app = typer.Typer()

@app.command()
def run(name: str):
    """Use to run the utility services.

    Args:
        name (str): The name of the utility process to run.
    """
    if name not in CONFIGS[UTILITY_SERVICES]:
        print(f'Service named "{name}" does not exists.')
        return

    subprocess.run([CONFIG_FILE_PATH / name])


@app.command()
def ls():
    """Lists the available utility services."""
    if not CONFIGS[UTILITY_SERVICES]:
        return

    print('Utility Services:')
    for s in CONFIGS[UTILITY_SERVICES]:
        print(f'  {s}')


if __name__ == '__main__':
    app()