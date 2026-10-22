from SPC_Subcode.read_txt_round import extract_all_info_from_all_rounds
from SPC_Subcode.find_player_and_teams import find_players_from_rounds





rounds = extract_all_info_from_all_rounds()
players = find_players_from_rounds(rounds)
print(players)