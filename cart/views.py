from django.shortcuts import render, redirect
from accounts.models import UserDetails
from products.models import Products

from .models import Cart, CartItem
# Create your views here.


def view_cart_items(request):
    id = request.session.get('User_id')
    if id:
        user = UserDetails.objects.get(id=id)
        cart = Cart.objects.get(user=user)
        if cart:
            cartitems = CartItem.objects.filter(cart=cart)
            total_price = 0
            products = []
            for item in cartitems:
                print(item.quantity)
                print(item.product.name)
                print(item.product.description)
                print(item.product.price)
                print("------------------------------------------------")
                total_price += item.product.price*item.quantity
                products.append((item.product, item.quantity))
                
        data = {'products': products, 'total_price': total_price}
        print(total_price)



    return render(request, 'cart/view_cart.html', context = data)

def add_to_cart(request, product_id):

    print(request.user)
    id = request.session.get('User_id')
    user = UserDetails.objects.get(id=id)
    cart, _ = Cart.objects.get_or_create(user=user)
    
    product = Products.objects.get(id=product_id)


    cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cartitem.quantity+=1
        cartitem.save()

        return redirect('cart:view_cart_items')
    

    return redirect('cart:view_cart_items')