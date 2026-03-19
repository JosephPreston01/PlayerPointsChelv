import requests
from config import ESPN_BASE_URL, WATCHED_PLAYERS


def fetch_player_points():
    """
    Fetches today's NCAA Tournament games and returns points for watched players.
    Returns a list of dicts: [{"player_name": "...", "points": 0}, ...]
    """
    scoreboard_url = f"{ESPN_BASE_URL}/scoreboard"
    resp = requests.get(scoreboard_url, params={"groups": "100"}, timeout=10)
    resp.raise_for_status()
    games = resp.json().get("events", [])

    watched_teams = {p["team"] for p in WATCHED_PLAYERS}
    watched_names = {p["name"] for p in WATCHED_PLAYERS}

    results = []

    for game in games:
        home    = game["competitions"][0]["competitors"][0]["team"]["displayName"]
        away    = game["competitions"][0]["competitors"][1]["team"]["displayName"]

        if not watched_teams.intersection({home, away}):
            continue

        game_id = game["id"]
        summary_url = f"{ESPN_BASE_URL}/summary"
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
                        pts = stats[pts_index] if pts_index < len(stats) else 0
                        results.append({"player_name": name, "points": pts})

    return results
