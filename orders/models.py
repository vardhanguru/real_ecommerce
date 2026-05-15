from django.db import models

from accounts.models import UserDetails
from products.models import Products


class Order(models.Model):

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    )


    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    address = models.TextField()

    phone_number = models.CharField(max_length=15)

    payment_method = models.CharField(max_length=20)

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    total_amount = models.FloatField()

    razorpay_order_id = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    razorpay_signature = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.payment_status}"


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name