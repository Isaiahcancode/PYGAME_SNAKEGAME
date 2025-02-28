import json
import os
SAVE_FILE = "game_save.json"
SAVE_DIR = 'saves'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
    
def save_game(username, game_data):
    """Saves game game_data to a file."""
    file_path = os.path.join(SAVE_DIR, f"{username}.json")
    with open(file_path, "w") as save_file:
        json.dump(game_data, save_file)


def load_game(username):
    file_path = os.path.join(SAVE_DIR, f"{username}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as save_file:
            return json.load(save_file)
    return None
