from django.contrib import admin
from .models import User
from . import models

admin.site.register(models.User)
