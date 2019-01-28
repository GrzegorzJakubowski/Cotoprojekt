from django.db import models

# Create your models here.

class koty(models.Model):
    nazwa = models.CharField(max_length=120)
    kraj = models.CharField(max_length=120)
    czy_gruby =models.BooleanField()