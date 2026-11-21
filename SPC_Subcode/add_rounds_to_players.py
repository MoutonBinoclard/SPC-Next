FALSE_ROUND = [
    {
        "pID": -2,
        "Player": "NON_PLAYED",
        "SquadID": -2,
        "TeamID": -2,
        "Kills": -2,
        "Placement": -2,
        "TrueScore": -2
    }
]



def add_rounds_to_players(rounds, players):
    """
    Add the rounds information to the players dictionary
    """

    for playfab_id, player in players.items():
        player["Rounds"] = []
        for round in rounds:
            if playfab_id in round:
                player["Rounds"].append(round[playfab_id])
            else:
                player["Rounds"].append(FALSE_ROUND[0].copy())
    return players