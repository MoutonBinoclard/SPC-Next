def find_players_from_rounds(rounds):
    """
    Extract all the players from all rounds and return them keyed by PlayFab ID
    """
    players = {}

    for round in rounds:
        for playfab_id, player_info in round.items():
            players[playfab_id] = {"Player": player_info["Player"]}

    return players