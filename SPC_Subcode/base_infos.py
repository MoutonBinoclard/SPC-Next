def extract_base_infos_form_rounds(rounds):
    """
    Extract base information from all rounds and return it as a dictionary
    """
    base_infos = {
        "Total_Rounds": len(rounds),
        "Nb_players_per_round": [],
        "Nb_spectator_per_round": [],
    }

    for round in rounds:
        nb_connected_account = len(round)
        nb_players = sum(1 for player_info in round.values() if player_info["Placement"] > 0)
        nb_spectator = nb_connected_account - nb_players

        base_infos["Nb_players_per_round"].append(nb_players)
        base_infos["Nb_spectator_per_round"].append(nb_spectator)

    return base_infos