import json
import os

def read_options():
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bots_path = os.path.join(project_path, "SPC_Data", "SPC_options.json")

    with open(bots_path, "r", encoding="utf-8-sig") as file:
        options = json.load(file)
    return options
