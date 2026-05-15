
from django.urls import path, include
from .views import order_page, payment_success, orders_details
app_name = 'orders'
urlpatterns = [
    path('orders_page/', order_page, name='order_page'),
    
    path(
        'payment-success/',
        payment_success,
        name='payment_success'
    ),
    path('ordersdetails/', orders_details, name='ordersdetails')

]

