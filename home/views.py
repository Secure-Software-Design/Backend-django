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



# Create your views here.

"""class StudentList(APIView):
    def get(self,request):
        students = models.Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)"""

class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def student_login(request):
    username=request.POST['username']
    password=request.POST['password']
    studentData=models.Student.objects.get(username=username,password=password)
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

    print(username, email, password)
    if len(password) > 20 or len(password) < 5 or len(email) == 0 or len(username) == 0 :
        return JsonResponse({'bool':False})

    models.Student.objects.create(username=username,password=password, email=email)

    return JsonResponse({'bool':True})
