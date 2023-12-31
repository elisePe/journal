from django.db import models
from django.contrib.auth.models import AbstractUser

class entrees(models.Model):
    date = models.fields.CharField(max_length=100)
    texte = models.fields.CharField(max_length=500)
    us_id = models.fields.IntegerField(default=0)
    nbr = models.fields.IntegerField(default=0)


class users(models.Model):
    name = models.fields.CharField(max_length=10)
    passw = models.fields.CharField(max_length=15)
    us_id = models.fields.IntegerField(default=0)