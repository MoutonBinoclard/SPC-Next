def add_rounds_to_players(rounds, players):
    """
    Add the rounds information to the players dictionary
    """

    # Add Rounds section to each player
    for playfab_id in players:
        players[playfab_id]["Rounds"] = []

    # Iterate for each round and add the round information to the corresponding player
    for round in rounds:
        for playfab_id, round_info in round.items():
            players[playfab_id]["Rounds"].append(round_info)