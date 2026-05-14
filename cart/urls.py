
from django.contrib import admin

from django.urls import path, include
from .views import add_to_cart, view_cart_items, remove_quantity, remove_product

app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<int:product_id>', add_to_cart, name = 'add_to_cart'),
    path('remove_quantity/<int:product_id>', remove_quantity, name = 'remove_quantity'),
    path('view_cart_items/', view_cart_items, name='view_cart_items'),
    path('remove_product/<int:product_id>', remove_product, name='remove_product'),

]
