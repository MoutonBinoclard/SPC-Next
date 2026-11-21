def show_players(players):
    for KEYS in players :
        print(players[KEYS]['Player'])
        for round in players[KEYS]['Rounds']:
            print(round)