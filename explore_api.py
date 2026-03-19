"""
explore_api.py

Scratch script to validate ESPN API response shape.
Uses a hardcoded past date (Big Ten tournament) so we can inspect
real box score data without waiting for March Madness to start.

Run:  python explore_api.py
"""

import requests

BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball"

# A day during the Big Ten tournament — change if you want a different date
TEST_DATE = "20260313"

# Players to search for across all games on this date
TEST_PLAYERS = [
    {"name": "Bruce Thornton",  "team": "Ohio State"},
    {"name": "Cameron Boozer",  "team": "Duke"},
    {"name": "Jaden Bradley",   "team": "Arizona"},
]


# ── STEP 1: Fetch the scoreboard for the test date ────────────────────────────

print(f"\n{'='*60}")
print(f"SCOREBOARD for {TEST_DATE}")
print('='*60)

scoreboard_url = f"{BASE_URL}/scoreboard"
resp = requests.get(scoreboard_url, params={"dates": TEST_DATE}, timeout=10)
resp.raise_for_status()
scoreboard = resp.json()

games = scoreboard.get("events", [])
print(f"Total games found: {len(games)}\n")

for game in games:
    game_id = game["id"]
    status  = game["status"]["type"]["name"]
    home    = game["competitions"][0]["competitors"][0]["team"]["displayName"]
    away    = game["competitions"][0]["competitors"][1]["team"]["displayName"]
    print(f"  [{game_id}]  {away} vs {home}  —  {status}")

if not games:
    print("\nNo games found for this date. Try a different TEST_DATE.")
    exit()


# ── STEP 2: Search all games for watched players ──────────────────────────────

print(f"\n{'='*60}")
print("SEARCHING ALL GAMES FOR WATCHED PLAYERS")
print('='*60)

watched_teams = {p["team"] for p in TEST_PLAYERS}
watched_names = {p["name"] for p in TEST_PLAYERS}

found = []

for game in games:
    game_id = game["id"]
    home    = game["competitions"][0]["competitors"][0]["team"]["displayName"]
    away    = game["competitions"][0]["competitors"][1]["team"]["displayName"]

    if not watched_teams.intersection({home, away}):
        continue

    summary_url = f"{BASE_URL}/summary"
    resp = requests.get(summary_url, params={"event": game_id}, timeout=10)
    resp.raise_for_status()
    summary = resp.json()

    for team_block in summary.get("boxscore", {}).get("players", []):
        for stat_block in team_block.get("statistics", []):
            labels = stat_block.get("labels", [])
            if "PTS" not in labels:
                continue
            pts_index = labels.index("PTS")
            for entry in stat_block.get("athletes", []):
                name  = entry.get("athlete", {}).get("displayName", "?")
                stats = entry.get("stats", [])
                if name in watched_names:
                    pts = stats[pts_index] if pts_index < len(stats) else "N/A"
                    print(f"  {name}: {pts} pts  ({away} vs {home}, game {game_id})")
                    found.append(name)

if not found:
    print("\n  None of the watched players found on this date.")
    print("  They may not have played — try a date when their team had a game.")
