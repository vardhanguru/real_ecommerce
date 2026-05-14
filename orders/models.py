from django.db import models

# Create your models here.

from accounts.models import UserDetails

from products.models import Products


class Order(models.Model):

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    address = models.CharField()
    phone_number = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_method = models.CharField()
    payment_status = models.CharField(default = 'Pending')

    total_amount = models.FloatField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    poduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
