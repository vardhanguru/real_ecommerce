
from django.contrib import admin

from django.urls import path, include
from .views import add_to_cart, view_cart_items

app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<int:product_id>', add_to_cart, name = 'add_to_cart'),
    path('view_cart_items/', view_cart_items, name='view_cart_items')

]
