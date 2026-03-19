from read_scores import fetch_player_points
from sheets import get_current_round, write_points

round_number = get_current_round()
if not round_number:
    print("No tournament games today.")
    exit()

results = fetch_player_points()
if not results:
    print("No player data found.")
    exit()

write_points(results, round_number)
print(f"Updated {len(results)} player(s) for round {round_number}.")
