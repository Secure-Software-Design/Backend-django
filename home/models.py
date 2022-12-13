from django.db import models

# Create your models here.
# Remove / Add something; Steps : 
# 1 serializers, update
# python3 manage.py makemigrations
# python3 manage.py migrate


class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    
    #class Meta:
        #verbrose_name_plural = "1. Students"
