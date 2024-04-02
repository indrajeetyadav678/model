from django.db import models

# Create your models here.
class Login(models.Model):
    Name=models.CharField(max_length=100)
    password=models.IntegerField()
    Email=models.CharField(max_length=70)