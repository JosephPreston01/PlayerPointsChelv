import os
from dotenv import load_dotenv

load_dotenv()

# Google Sheets
GOOGLE_SHEET_ID   = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_CREDS_FILE = os.getenv("GOOGLE_CREDS_FILE", "credentials.json")

# ESPN API
ESPN_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball"

# Tournament date window (inclusive)
# NOTE: Tournament began March 19, 2026 (Round of 64 Day 1). Dates were
# previously off by one — corrected on 2026-03-19 after first dispatch showed
# no games due to ROUND_DATES starting on the 20th.
TOURNAMENT_START = "2026-03-19"
TOURNAMENT_END   = "2026-04-07"

# Maps round number to the dates it is played (used to determine current column)
ROUND_DATES = {
    1: ["2026-03-19", "2026-03-20"],  # Round of 64
    2: ["2026-03-21", "2026-03-22"],  # Round of 32
    3: ["2026-03-26", "2026-03-27"],  # Sweet 16
    4: ["2026-03-28", "2026-03-29"],  # Elite 8
    5: ["2026-04-04"],                # Final Four
    6: ["2026-04-06"],                # Championship
}

# Game hours in ET (noon to midnight)
GAME_WINDOW_START_HOUR = 12
GAME_WINDOW_END_HOUR   = 23

WATCHED_PLAYERS = [
  {"name": "Cameron Boozer",       "team": "Duke Blue Devils"},
  {"name": "Boogie Fland",         "team": "Florida Gators"},
  {"name": "Aday Mara",            "team": "Michigan Wolverines"},
  {"name": "Meleek Thomas",        "team": "Arkansas Razorbacks"},
  {"name": "Cayden Boozer",        "team": "Duke Blue Devils"},
  {"name": "Donovan Dent",         "team": "UCLA Bruins"},
  {"name": "Latrell Wrightsell",   "team": "Alabama Crimson Tide"},
  {"name": "Seth Trimble",         "team": "North Carolina Tar Heels"},
  {"name": "Thomas Dowd",          "team": "Troy Trojans"},
  {"name": "Robbie Avila",         "team": "Saint Louis Billikens"},

  {"name": "Brayden Burries",      "team": "Arizona Wildcats"},
  {"name": "Jeremy Fears Jr.",     "team": "Michigan State Spartans"},
  {"name": "Ivan Kharchenkov",     "team": "Arizona Wildcats"},
  {"name": "Mikey Lewis",          "team": "Saint Mary's Gaels"},
  {"name": "David Mirkovic",       "team": "Illinois Fighting Illini"},
  {"name": "Malik Thomas",         "team": "Virginia Cavaliers"},
  {"name": "Otega Oweh",           "team": "Kentucky Wildcats"},
  {"name": "Malik Reneau",         "team": "Miami Hurricanes"},
  {"name": "Alex Wilkins",         "team": "Furman Paladins"},
  {"name": "Tavari Johnson",       "team": "Akron Zips"},

  {"name": "Thomas Haugh",         "team": "Florida Gators"},
  {"name": "Graham Ike",           "team": "Gonzaga Bulldogs"},
  {"name": "Darryn Peterson",      "team": "Kansas Jayhawks"},
  {"name": "John Blackwell",       "team": "Wisconsin Badgers"},
  {"name": "Ja'Kobi Gillespie",    "team": "Tennessee Volunteers"},
  {"name": "Cruz Davis",           "team": "Hofstra Pride"},
  {"name": "Henri Veesaar",        "team": "North Carolina Tar Heels"},
  {"name": "Paulius Murauskas",    "team": "Saint Mary's Gaels"},
  {"name": "Tre Donaldson",        "team": "Miami Hurricanes"},
  {"name": "Roddy Gayle Jr.",      "team": "Michigan Wolverines"},

  {"name": "Yaxel Lendeborg",      "team": "Michigan Wolverines"},
  {"name": "Braden Smith",         "team": "Purdue Boilermakers"},
  {"name": "Tamin Lipsey",         "team": "Iowa State Cyclones"},
  {"name": "Solo Ball",            "team": "UConn Huskies"},
  {"name": "Milos Uzan",           "team": "Houston Cougars"},
  {"name": "Alex Karaban",         "team": "UConn Huskies"},
  {"name": "Tomislav Ivisic",      "team": "Illinois Fighting Illini"},
  {"name": "Bruce Thornton",       "team": "Ohio State Buckeyes"},
  {"name": "Coen Carr",            "team": "Michigan State Spartans"},
  {"name": "Michael Cooper",       "team": "Wright State Raiders"},

  {"name": "Darius Acuff Jr.",     "team": "Arkansas Razorbacks"},
  {"name": "Emanuel Sharp",        "team": "Houston Cougars"},
  {"name": "AJ Dybantsa",          "team": "BYU Cougars"},
  {"name": "Zuby Ejiofor",         "team": "St. John's Red Storm"},
  {"name": "Duke Miles",           "team": "Vanderbilt Commodores"},
  {"name": "Andrej Stojakovic",    "team": "Illinois Fighting Illini"},
  {"name": "Braylon Mullins",      "team": "UConn Huskies"},
  {"name": "Tyler Bilodeau",       "team": "UCLA Bruins"},
  {"name": "Tyon Grant-Foster",    "team": "Gonzaga Bulldogs"},
  {"name": "Victor Valdez",        "team": "Troy Trojans"},

  {"name": "Kingston Flemings",    "team": "Houston Cougars"},
  {"name": "Morez Johnson Jr.",    "team": "Michigan Wolverines"},
  {"name": "Thijs De Ridder",      "team": "Virginia Cavaliers"},
  {"name": "Pryce Sandfort",       "team": "Nebraska Cornhuskers"},
  {"name": "Tarris Reed Jr.",      "team": "UConn Huskies"},
  {"name": "Dominque Daniels",     "team": "California Baptist Lancers"},
  {"name": "Ryan Conwell",         "team": "Louisville Cardinals"},
  {"name": "Anthony Dell'Orso",    "team": "Arizona Wildcats"},
  {"name": "Oscar Cluff",          "team": "Purdue Boilermakers"},
  {"name": "Jeremiah Wilkinson",   "team": "Georgia Bulldogs"},

  {"name": "Isaiah Evans",         "team": "Duke Blue Devils"},
  {"name": "Alex Condon",          "team": "Florida Gators"},
  {"name": "Fletcher Loyer",       "team": "Purdue Boilermakers"},
  {"name": "Kylan Boswell",        "team": "Illinois Fighting Illini"},
  {"name": "Nate Ament",           "team": "Tennessee Volunteers"},
  {"name": "Jaxon Kohler",         "team": "Michigan State Spartans"},
  {"name": "Nimari Burnett",       "team": "Michigan Wolverines"},
  {"name": "Billy Richmond III",   "team": "Arkansas Razorbacks"},
  {"name": "Silas Demary Jr.",     "team": "UConn Huskies"},
  {"name": "Aaron Nkrumah",        "team": "Tennessee State Tigers"},

  {"name": "Labaron Philon Jr.",   "team": "Alabama Crimson Tide"},
  {"name": "Keaton Wagler",        "team": "Illinois Fighting Illini"},
  {"name": "Motiejus Krivas",      "team": "Arizona Wildcats"},
  {"name": "Nick Boyd",            "team": "Wisconsin Badgers"},
  {"name": "Rueben Chinyelu",      "team": "Florida Gators"},
  {"name": "Tobe Awaka",           "team": "Arizona Wildcats"},
  {"name": "Trey McKenney",        "team": "Michigan Wolverines"},
  {"name": "Bennett Stirtz",       "team": "Iowa Hawkeyes"},
  {"name": "Tre White",            "team": "Kansas Jayhawks"},
  {"name": "RJ Johnson",           "team": "Kennesaw State Owls"},

  {"name": "Koa Peat",             "team": "Arizona Wildcats"},
  {"name": "Joshua Jefferson",     "team": "Iowa State Cyclones"},
  {"name": "Tyler Tanner",         "team": "Vanderbilt Commodores"},
  {"name": "Christian Anderson",   "team": "Texas Tech Red Raiders"},
  {"name": "Robert Wright III",    "team": "BYU Cougars"},
  {"name": "Trevon Brazile",       "team": "Arkansas Razorbacks"},
  {"name": "Donovan Atwell",       "team": "Texas Tech Red Raiders"},
  {"name": "Sam Lewis",            "team": "Virginia Cavaliers"},
  {"name": "Mark Mitchell",        "team": "Missouri Tigers"},
  {"name": "Isaac Johnson",        "team": "Hawai'i Rainbow Warriors"},

  {"name": "Jaden Bradley",        "team": "Arizona Wildcats"},
  {"name": "Milan Momcilovic",     "team": "Iowa State Cyclones"},
  {"name": "Xaivian Lee",          "team": "Florida Gators"},
  {"name": "Trey Kaufman-Renn",    "team": "Purdue Boilermakers"},
  {"name": "Elliot Cadeau",        "team": "Michigan Wolverines"},
  {"name": "Bryce Hopkins",        "team": "St. John's Red Storm"},
  {"name": "Chris Cenac Jr.",      "team": "Houston Cougars"},
  {"name": "Preston Edmead",       "team": "Hofstra Pride"},
  {"name": "Carson Cooper",        "team": "Michigan State Spartans"},
  {"name": "Tyler Nickel",         "team": "Vanderbilt Commodores"},
]