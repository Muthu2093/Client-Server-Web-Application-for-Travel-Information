from django.db import models
from django_mysql.models import JSONField, Model

class bkup(models.Model):
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)

class MyModel(models.Model):
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    attrs = JSONField()
    weather = JSONField()
    date = models.DateField(auto_now=True)