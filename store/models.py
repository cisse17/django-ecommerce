from django.db import models
from django.utils.text import slugify 
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

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
    slug = models.SlugField(max_length=255, blank=True)    
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

    
# Article (Order)
"""
-Utilisateur
-Produit
-Quantité
- Commandé ou pas 
"""
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) "


# Panier (Cart)
"""
-Utilisateur
-articles
-commandé ou non
-date de la commande
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username