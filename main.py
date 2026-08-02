# TODO: Functionality to create, read, and write config data.
import json

UTILITY_FOLDER = './Utility'
CONFIG_FILE = 'config.json'

CONFIG = {
    'UTILITY_FOLDER': UTILITY_FOLDER
}

# Load configurations.
try:
    with open(CONFIG_FILE, 'r') as f:
        CONFIG = json.load(f)
except FileNotFoundError:
    with open(CONFIG_FILE, 'w') as f:
        json.dump(CONFIG, f)
except Exception as e:
    raise e

# TODO: Implement argument parsing.
