import requests
import json 

def getMatchs():
    res = requests.get('https://worldcupjson.net/matches/')
    response = json.loads(res.text)

    resultMatchs = {
        "first_stage":[],
        "round_of_16":[],
        "quarter_final":[],
        "semi_final":[],
        "third_place":[],
        "final":[],
    }

    for el in response:
        match =  {
            "match_id":-1,
            "team1":"",
            "team1_code":"",
            "team1_flag":"",
            "goal_team1":-1,
            "penalties_team1":-1,
            "team2":"",
            "team2_code":"",
            "team2_flag":"",
            "goal_team2":-1,
            "penalties_team2":-1,
            "winner":"",
            "winner_code":"",
            "date_time":"",
        }
        match["match_id"] = el["id"]
        team1 = el["home_team"]
        match["team1"] = team1["name"]
        match["team1_code"] = team1["country"]
        match["goal_team1"] = team1["goals"]
        match["penalties_team1"] = team1["penalties"]
        match["team1_flag"] = "https://countryflagsapi.com/png/" + team1["name"].lower()
        team2 = el["away_team"]
        match["team2"] = team2["name"]
        match["team2_code"] = team2["country"]
        match["team2_flag"] = "https://countryflagsapi.com/png/" + team2["name"].lower()
        match["goal_team2"] = team2["goals"]
        match["penalties_team2"] = team2["penalties"]
        match["winner"] = el["winner"]
        match["winner_code"] = el["winner_code"]
        match["date_time"] = el["datetime"]
        print(match)
        if el["stage_name"] == "First stage":
            resultMatchs["first_stage"].append(match)
        elif el["stage_name"] == "Round of 16":
            resultMatchs["round_of_16"].append(match)
        elif el["stage_name"] == "Quarter-final":
            resultMatchs["quarter_final"].append(match)
        elif el["stage_name"] == "Semi-final":
            resultMatchs["semi_final"].append(match)
        elif el["stage_name"] == "Play-off for third place":
            resultMatchs["third_place"].append(match)
        elif el["stage_name"] == "Final":
            resultMatchs["final"].append(match)
        else:
            print("ERROR STAGE NAME NOT FOUND : ", el["stage_name"] , "!!!!!\n") 

    print(json.dumps(resultMatchs , indent=4))
    



def getMatch(match_id):
    res = requests.get('https://worldcupjson.net/matches/' + str(match_id))
    response = json.loads(res.text)
    match =  {
            "match_id":-1,
            "team1":"",
            "team1_code":"",
            "goal_team1":-1,
            "penalties_team1":-1,
            "tactic_team1":"",
            "team2":"",
            "team2_code":"",
            "goal_team2":-1,
            "penalties_team2":-1,
            "tactic_team2":"",
            "winner":"",
            "winner_code":"",
            "date_time":"",
    }
    match["match_id"] = match_id
    team1 = response["home_team"]
    match["team1"] = team1["name"]
    match["team1_code"] = team1["country"]
    match["goal_team1"] = team1["goals"]
    match["penalties_team1"] = team1["penalties"]
    team2 = response["away_team"]
    match["team2"] = team2["name"]
    match["team2_code"] = team2["country"]
    match["goal_team2"] = team2["goals"]
    match["penalties_team2"] = team2["penalties"]
    match["winner"] = response["winner"]
    match["winner_code"] = response["winner_code"]
    match["date_time"] = response["datetime"]
    print(json.dumps(match, indent=4))
    
#getMatch(62)
getMatchs()