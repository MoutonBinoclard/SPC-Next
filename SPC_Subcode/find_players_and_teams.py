import os

def find_players_from_rounds(rounds):
    """
    Extract all the players from all rounds and return them keyed by PlayFab ID
    """

    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bots_path = os.path.join(project_path, "SPC_Data", "SPC_bots.json")

    players = {}

    for round in rounds:
        for playfab_id, player_info in round.items():
            players[playfab_id] = {"Player": player_info["Player"]}

    return players


def find_bot_id(player):
    """
    Search directly the PlayfabID of the bot in the SPC_bots.json to add the ID
    """
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bots_path = os.path.join(project_path, "SPC_Data", "SPC_bots.json")

    with open(bots_path, "r", encoding="utf-8-sig") as file:
        bots = json.load(file)

    for bot in bots:
        if bot["Player"] == player:
            return bot["PlayfabID"]