from django.db import models


# Create your models here.

class Product1(models.Model):
    fullname = models.CharField(max_length=100)
    price = models.FloatField()
    detail = models.CharField(max_length=500)

#CRUD


