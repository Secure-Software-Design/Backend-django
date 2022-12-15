from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# Remove / Add something; Steps : 
# 1 serializers, update
# python3 manage.py makemigrations
# python3 manage.py migrate


class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

def validate_match_id(value):
    if value < 1:
        raise ValidationError("Match ID must be greater than 0")
    if value > 64:
        raise ValidationError("Match ID must be less than 65")

def validate_code_length(value):
    if value != value.upper():
        raise ValidationError("Country code must be capitalised")
    if len(str(value))!= 3:
        raise ValidationError(u'%s is not the correct length for a Country Code' % value)

def validate_scrore(value):
    if  value < 0:
        raise ValidationError("Score cannot be negative")


class Matchs(models.Model):
    match_id = models.IntegerField(primary_key=True, unique=True, null=False, blank=False, validators=[validate_match_id])
    team1 = models.CharField(max_length=30),
    team1_code = models.CharField(max_length=3, validators=[validate_code_length]),
    goal_team1 = models.IntegerField(validators=[validate_scrore]),
    penalty_team1 = models.IntegerField(validators=[validate_scrore]),
    team2 = models.CharField(max_length=30),
    team2_code = models.CharField(max_length=3, validators=[validate_code_length]),
    goal_team2 = models.IntegerField(validators=[validate_scrore]),
    penalty_team2 = models.IntegerField(validators=[validate_scrore]),
    winner = models.CharField(max_length=30),
    winner_code = models.CharField(max_length=3, validators=[validate_code_length]),
    date_time = models.DateTimeField(),

    
    #class Meta:
        #verbrose_name_plural = "1. Students"
