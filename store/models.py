from django.db import models


"""
Product :
nom 
prix  (int/float)
quantité en stock (int)
description (TextField)
image (ImageField)
"""
class Product(models.Model):
    name = models.CharField(max_length=255)
    prix = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name