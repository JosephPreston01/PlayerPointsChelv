import os
from datetime import date

import gspread
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from config import GOOGLE_SHEET_ID, GOOGLE_CREDS_FILE, WATCHED_PLAYERS, ROUND_DATES

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Player name → index lookup, built once at import time
PLAYER_INDEX = {p["name"]: i for i, p in enumerate(WATCHED_PLAYERS)}


def get_current_round():
    """Returns the round number (1-6) for today's date, or None if no games today."""
    today = date.today().strftime("%Y-%m-%d")
    for round_num, dates in ROUND_DATES.items():
        if today in dates:
            return round_num
    return None


def _get_client():
    """Handles OAuth flow. Opens browser on first run, uses token.json after that."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(GOOGLE_CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return gspread.authorize(creds)


def _player_row(player_index):
    """
    Calculates the sheet row for a player given their index in WATCHED_PLAYERS.
    Layout: repeating blocks of 1 block header + 10 players + 1 extra row (12 rows total per block).
    """
    block = player_index // 10
    pos   = player_index % 10
    return block * 12 + pos + 2  # +1 for block header in first block; +3 per subsequent block (extra row + next block header + player)


def write_points(results, round_number):
    """
    Writes player points to the correct round column in the sheet.
    results: list of {"player_name": str, "points": int}
    round_number: int 1-6
    """
    client = _get_client()
    sheet  = client.open_by_key(GOOGLE_SHEET_ID).sheet1

    col = round_number + 1  # Col A = names, Col B = Round 1, Col C = Round 2, etc.

    for result in results:
        name = result["player_name"]
        pts  = result["points"]

        if name not in PLAYER_INDEX:
            continue

        row = _player_row(PLAYER_INDEX[name])
        sheet.update_cell(row, col, pts)
