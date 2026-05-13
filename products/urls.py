from django.contrib import admin
from django.urls import path
from .views import all_products, product_details
app_name = 'products'
urlpatterns = [
    path('', all_products, name = 'ecommercehome'),
    path('product/<int:id>', product_details, name = 'product-details'),
]
