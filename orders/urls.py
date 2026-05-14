
from django.urls import path, include
from .views import order_page
app_name = 'orders'
urlpatterns = [
    path('orders_page/', order_page, name='order_page')
]

