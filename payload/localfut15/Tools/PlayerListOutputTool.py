import json
from pathlib import Path

from numpy import info


ROOT = Path(__file__).resolve().parent.parent


PLAYER_DB = {
    20801:  {"name":"Cristiano Ronaldo","rating":92,"preferredPosition":"LW","leagueId":53,"teamid":243,"nation":38,"face":[93,93,81,91,32,79]},
    158023: {"name":"Lionel Messi","rating":93,"preferredPosition":"CF","leagueId":53,"teamid":241,"nation":52,"face":[93,89,86,96,27,62]},
    190871: {"name":"Neymar Jr","rating":86,"preferredPosition":"LW","leagueId":53,"teamid":241,"nation":54,"face":[90,80,72,92,30,58]},
    176580: {"name":"Luis Suarez","rating":89,"preferredPosition":"ST","leagueId":53,"teamid":241,"nation":60,"face":[83,87,79,88,42,79]},
    173731: {"name":"Gareth Bale","rating":87,"preferredPosition":"RM","leagueId":53,"teamid":243,"nation":50,"face":[94,83,83,84,63,81]},
    188545: {"name":"Robert Lewandowski","rating":87,"preferredPosition":"ST","leagueId":19,"teamid":21,"nation":37,"face":[81,84,74,85,39,78]},
    153079: {"name":"Sergio Aguero","rating":86,"preferredPosition":"ST","leagueId":13,"teamid":10,"nation":52,"face":[88,86,77,88,28,66]},
    183277: {"name":"Eden Hazard","rating":88,"preferredPosition":"LM","leagueId":13,"teamid":5,"nation":7,"face":[89,82,84,91,32,64]},
    167495: {"name":"Manuel Neuer","rating":90,"preferredPosition":"GK","leagueId":19,"teamid":21,"nation":21,"face":[87,85,92,86,58,90]},
    155862: {"name":"Sergio Ramos","rating":87,"preferredPosition":"CB","leagueId":53,"teamid":243,"nation":45,"face":[79,60,71,66,87,82]},
    164240: {"name":"Thiago Silva","rating":87,"preferredPosition":"CB","leagueId":16,"teamid":73,"nation":54,"face":[78,57,72,72,90,80]},
    177003: {"name":"Luka Modric","rating":87,"preferredPosition":"CM","leagueId":53,"teamid":243,"nation":10,"face":[76,74,85,89,71,70]},
    182521: {"name":"Toni Kroos","rating":85,"preferredPosition":"CM","leagueId":53,"teamid":243,"nation":21,"face":[58,81,89,84,58,69]},
    195864: {"name":"Paul Pogba","rating":83,"preferredPosition":"CM","leagueId":31,"teamid":45,"nation":18,"face":[76,78,79,83,73,88]},
}

PLAYER_DB_PATH = ROOT / "players.json"

if PLAYER_DB_PATH.exists():
    try:
        raw_player_db = json.loads(PLAYER_DB_PATH.read_text(encoding="utf-8"))
        if isinstance(raw_player_db, dict):
            for rid, meta in raw_player_db.items():
                if isinstance(meta, dict):
                    PLAYER_DB[int(rid)] = meta
        log_player_count = len(PLAYER_DB)
    except Exception:
        log_player_count = len(PLAYER_DB)
else:
    print("Can't find file at path")
    print(PLAYER_DB_PATH)
    log_player_count = len(PLAYER_DB)



print("Input min rating")
RatingStart = input(int)

print("Input max rating")
RatingEnd = input(int)

print("Input prefered position")
PreferredPosition = input(str)

OUTPUT_PLAYER_DB = []

OUTPUT_PLAYER_DB.clear()

for player in PLAYER_DB:
    if(PLAYER_DB[player].get("rating") >= int(RatingStart) and PLAYER_DB[player].get("rating") <= int(RatingEnd) and PLAYER_DB[player].get("preferredPosition") == str(PreferredPosition)):
        OUTPUT_PLAYER_DB.append(player)
    

print(OUTPUT_PLAYER_DB)