from django.db import models
from django.utils.text import slugify 
from django.urls import reverse

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
    slug = models.SlugField(max_length=255, unique=True)    
    prix = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)