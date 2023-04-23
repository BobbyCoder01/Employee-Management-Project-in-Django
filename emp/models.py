from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=20)
    address = models.CharField(max_length=100)
    working = models.BooleanField(default=True)
    
