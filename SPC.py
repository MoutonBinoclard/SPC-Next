from SPC_Subcode.read_options import read_options
from SPC_Subcode.read_txt_round import extract_all_info_from_all_rounds
from SPC_Subcode.find_players_and_teams import find_players_from_rounds
from SPC_Subcode.base_infos import extract_base_infos_form_rounds
from SPC_Subcode.add_rounds_to_players import add_rounds_to_players

from SPC_Subcode.UTIL import *


# Loading options
OPTIONS = read_options()
INCLUDE_BOTS = OPTIONS.get("INCLUDE_BOTS", False)



# Extracting rounds and all players from every round as well base information on the tournament
rounds = extract_all_info_from_all_rounds(INCLUDE_BOTS)
players = find_players_from_rounds(rounds)
infos = extract_base_infos_form_rounds(rounds)


# Adding all rounds to each player
players = add_rounds_to_players(rounds, players)

show_players(players)