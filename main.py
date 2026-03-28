import argparse
from read_scores import fetch_player_points
from sheets import get_current_round, write_points

parser = argparse.ArgumentParser()
parser.add_argument("--date", help="Date to fetch scores for (YYYY-MM-DD). Defaults to today.")
args = parser.parse_args()

# Normalize YYYY-MM-DD → YYYYMMDD for internal use
date = args.date.replace("-", "") if args.date else None

round_number = get_current_round(date)
if not round_number:
    print("No tournament games today.")
    exit()

results = fetch_player_points(date)
if not results:
    print("No player data found.")
    exit()

write_points(results, round_number)
print(f"Updated {len(results)} player(s) for round {round_number}.")
