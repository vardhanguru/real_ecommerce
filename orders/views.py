from django.shortcuts import render
from accounts.models import UserDetails
from cart.models import Cart, CartItem
from products.models import Products

# Create your views here.


def order_page(request, ):
    # if im proceeding from cart page, all cartitems...

    # need to create the order
    id = request.session.get('User_id')
    user = UserDetails.objects.get(id=id)
    cart = Cart.objects.get(user=user)
    cartitems = CartItem.objects.filter(cart=cart)
    total_price = 0
    products = []
    for item in cartitems:
        print(item.quantity)
        print(item.product.name)
        item.product.image = str(item.product.image)[7:]   #static/images/iphone.jpg
        print(item.product.description)
        print(item.product.price)
        print("------------------------------------------------")
        total_price += item.product.price*item.quantity
        products.append((item.product, item.quantity))


    data = {'cartitems': cartitems, 'total_price': total_price, 'user': user}


    if request.method=="POST":
        pass
        # create the order details.....

    return render(request, 'orders/orders_page.html', context=data)