from django.test import TestCase
import re
import requests
import json

# coverage run -m pytest
# coverage report

def user_register(inputUsername, password, inputEmail):
    patternUsername = "^[a-zA-Z0-9_-]{3,15}$"
    patternEmail = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    
    username = re.findall(patternUsername, inputUsername)
    email = re.findall(patternEmail, inputEmail)

    print(username, email, password)
    if len(password) > 20 or len(password) < 5 or len(email) == 0 or len(username) == 0 :
        return False

    return True


def user_login(error):
    
    print("Mock call to DB to search for student login information")
    if error:
        return True
    else:
        return False


def getMatchs(request):
    try:
        res = requests.get(request)
        response = json.loads(res.text)
    except:
        print("Internal error")
        return 1
    



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
        match["match_id"] = el["id"] # pragma: no cover
        team1 = el["home_team"] # pragma: no cover
        match["team1"] = team1["name"] # pragma: no cover
        match["team1_code"] = team1["country"] # pragma: no cover
        match["goal_team1"] = team1["goals"] # pragma: no cover
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
    return 0


# Create your tests here.

def test_register_good_data():
    assert user_register('semaphore', 'StrongPassw0rd*', "good@email.com") == True


def test_register_bad_username():
    assert user_register('Ju', 'StrongPassw0rd*', "good@email.com") == False


def test_register_bad_password():
    assert user_register('semaphore', 'ok*', "good@email.com") == False


def test_register_bad_email():
    assert user_register('semaphore', 'StrongPassw0rd*', "bad") == False


def test_login():
    assert user_login(True) == True


def test_login_failure():
    assert user_login(False) == False


def test_get_matchs_success():
    assert getMatchs("https://worldcupjson.net/matches/") == 0


def test_get_matchs_failure():
    assert getMatchs("") == 1

