from django.db import models
from django.forms import ModelForm
from django.core import validators

class Beat(models.Model):
    beat = models.CharField(max_length=1000)


class Record(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    recommendations = models.CharField(max_length=300)
    unique = models.IntegerField()
    #heart_beat = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'recommendations', 'unique']