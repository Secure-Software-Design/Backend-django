from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from . import models
import re
import requests
import json 


# Create your views here.

"""class StudentList(APIView):
    def get(self,request):
        students = models.User.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)"""

class StudentList(generics.ListCreateAPIView):
    queryset=models.User.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.User.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def student_login(request):
    username=request.POST['username']
    password=request.POST['password']
    studentData=models.User.objects.get(username=username,password=password)
    if studentData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool': False})


@csrf_exempt
def student_register(request):
    inputUsername=request.POST['username']
    password=request.POST['password']
    inputEmail=request.POST['email']
    patternUsername = "^[a-zA-Z0-9_-]{3,15}$"
    patternEmail = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    
    username = re.findall(patternUsername, inputUsername)
    email = re.findall(patternEmail, inputEmail)

    if len(password) > 20 or len(password) < 5 or len(email) == 0 or len(username) == 0 :
        return JsonResponse({'bool':False})

    models.User.objects.create(username=username[0],password=password, email=email[0])

    return JsonResponse({'bool':True})



def getMatchs(request):
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
    return JsonResponse(resultMatchs)