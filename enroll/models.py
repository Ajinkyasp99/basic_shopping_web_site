from django.db import models


# Create your models here.
class User(models.Model):
    product = models.CharField(max_length=70)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
