from django.db import models
from django.core import validators

class TempModel(models.Model):
   # date = models.DateTimeField(auto_now=False)
    room = models.CharField(max_length=20)
    temperature_f = models.FloatField(max_length=5)
    humidity = models.FloatField(max_length=5)
