from sheets import _get_client, _player_row, PLAYER_INDEX
from config import GOOGLE_SHEET_ID

# Hardcoded test values
TEST_ROUND   = 1  # Round of 64 = column B
TEST_PLAYERS = [
    ("Cameron Boozer",  25),
    ("Bruce Thornton",  18),
    ("Jaden Bradley",   22),
    ("AJ Dybantsa",     30),
    ("Tyler Nickel",    12),
]

client = _get_client()
sheet  = client.open_by_key(GOOGLE_SHEET_ID).worksheet("Copy of Sheet1")

col = TEST_ROUND + 1

for name, pts in TEST_PLAYERS:
    row = _player_row(PLAYER_INDEX[name])
    sheet.update_cell(row, col, pts)
    print(f"Wrote {pts} pts for {name} at row {row}, col {col}.")
