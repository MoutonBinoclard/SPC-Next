import os
import json

def find_rounds_path():
    """
    Return the path for all the rounds in SPC_Rounds in a list
    """
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rounds_path = os.path.join(project_path, "SPC_Rounds")

    return [
        os.path.join(rounds_path, filename)
        for filename in sorted(os.listdir(rounds_path))
        if filename.lower().endswith(".txt")
        and os.path.isfile(os.path.join(rounds_path, filename))
    ]

def find_bot_id(player):
    """
    Search directly the PlayfabID of the bot in the SPC_bots.json to add the ID
    """
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bots_path = os.path.join(project_path, "SPC_Subcode", "SPC_bots.json")

    with open(bots_path, "r", encoding="utf-8-sig") as file:
        bots = json.load(file)

    for bot in bots:
        if bot["Player"] == player:
            return bot["PlayfabID"]


def extract_all_info_from_round(round_path, bots=False):
    """
    Extract all the information from a round file and return it as a dictionary
    """
    round_info = {}

    # Open the round file and read its contents
    with open(round_path, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    # Skip header line and process each subsequent line
    for line_number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue

        # Split values by tab
        values = line.rstrip("\r\n").split("\t")

        p_id = values[0]
        player = values[1]
        playfab_id = values[-6]
        squad_id = values[-5]
        team_id = values[-4]
        kills = values[-3]
        placement = values[-2]
        true_score = values[-1]

        if playfab_id == "":
            if not bots:
                continue
            playfab_id = find_bot_id(player)

        round_info[playfab_id] = {
            "pID": p_id,
            "Player": player,
            "SquadID": squad_id,
            "TeamID": team_id,
            "Kills": kills,
            "Placement": placement,
            "TrueScore": true_score,
        }

    return round_info

def extract_all_info_from_all_rounds(bots=False):
    """
    Extract all the information from all round files and return it as a dictionary
    """
    rounds=[]
    rounds_path = find_rounds_path()
    for round_path in rounds_path:
        round_info = extract_all_info_from_round(round_path, bots)
        rounds.append(round_info)

    return rounds
