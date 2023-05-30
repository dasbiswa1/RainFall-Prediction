from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class weather(models.Model):
    district=models.CharField(max_length=100);
    year=models.CharField(max_length=100);
    rainfall=models.IntegerField();

def __str__(self):
    return self.district
    
