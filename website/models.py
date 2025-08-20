from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    category = models.CharField(max_length=50)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart {self.cart_id} - {self.product.product_name}"

