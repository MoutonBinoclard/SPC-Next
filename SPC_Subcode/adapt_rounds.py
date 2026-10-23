# {'EE08F0A1FD45935E': {'pID': '1', 'Player': 'ДЭНЧ', 'SquadID': '0', 'TeamID': '-1', 'Kills': '9', 'Placement': '4', 'TrueScore': '1'}, 'A7058E8647081049': {'pID': '2', 'Player': 'Eason·Chan', 'SquadID': '0', 'TeamID': '-1', 'Kills': '9', 'Placement': '4', 'TrueScore': '1'}, '53F9EFB9912B04AE': {'pID': '3', 'Player': 'Mouton Binoclard', 'SquadID': '1','TeamID': '-1', 'Kills': '3', 'Placement': '64', 'TrueScore': '18'}, '31387A9F6EC0AB4F': {'pID': '4', 'Player': '『MR』ツFADELツKING', 'SquadID': '0', 'TeamID': '-1', 'Kills': '1', 'Placement': '4', 'TrueScore': '1'}, '265A43EBAC58A25A': {'pID': '5', 'Player': 'Solo-Luki', 'SquadID': '0', 'TeamID': '-1', 'Kills': '8', 'Placement': '4', 'TrueScore': '1'}, '15F26C702F4BAF69': {'pID': '6', 'Player': 'oliverisagoof', 'SquadID': '3', 'TeamID': '-1', 'Kills': '1', 'Placement': '5', 'TrueScore': '2'}, '2BE3188F36174B3F': {'pID': '7', 'Player': 'lemonjumps', 'SquadID': '3', 'TeamID': '-1','Kills': '0', 'Placement': '5', 'TrueScore': '2'}, 'FB9AE857208E1605': {'pID': '8', 'Player': 'Cain <3', 'SquadID': '2', 'TeamID': '-1', 'Kills': '0', 'Placement': '32', 'TrueScore': '12'}, '601E0394211E6EFB': {'pID': '9', 'Player': 'nasabobu', 'SquadID': '3', 'TeamID': '-1', 'Kills': '0', 'Placement': '5', 'TrueScore': '2'}}

def analyse_round(round_data):
    """
    Find more information about a match
    For each entry in the dictionnary
    "Team_Members" : [PlayfabID1, PlayfabID2, ...] (list of all players in the team)
    "Team_Kills" : int (total kills of the team)
    "Masterkill_solo" : bool
    "Masterkill_team" : bool
    """

    # Team dictionnary
    squads = {}
    for player_id, player_info in round_data.items():

        SquadID = player_info["SquadID"]
        if SquadID not in squads:
            squads[SquadID] = []

        squads[SquadID].append(player_id)


    # Now for each team 