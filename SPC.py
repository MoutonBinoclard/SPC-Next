from SPC_Subcode.read_options import read_options
from SPC_Subcode.read_txt_round import extract_all_info_from_all_rounds
from SPC_Subcode.find_players_and_teams import find_players_from_rounds
from SPC_Subcode.adapt_rounds import analyse_round


# Loading options
OPTIONS = read_options()
INCLUDE_BOTS = OPTIONS.get("INCLUDE_BOTS", False)


rounds = extract_all_info_from_all_rounds(INCLUDE_BOTS)
players = find_players_from_rounds(rounds)

analyse_round(rounds[0])