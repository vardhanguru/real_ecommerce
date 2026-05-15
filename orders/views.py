from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

import razorpay

from accounts.models import UserDetails

from cart.models import Cart, CartItem

from .models import Order, OrderItem

def orders_details(request):
    user_id = request.session.get('User_id')
    user = UserDetails.objects.get(id=user_id)
    orders = Order.objects.filter(user_id=user_id).order_by('-id')
    d = []
    for order in orders:
        orderItems = OrderItem.objects.filter(order=order)
        
        d.append({'orderItems': orderItems, 'order': order})

    data = {'d': d}

    return render(request, 'orders/orders.html', context = data)



def order_page(request):

    id = request.session.get('User_id')

    if not id:
        return redirect('login')

    user = UserDetails.objects.get(id=id)

    cart = Cart.objects.get(user=user)

    cartitems = CartItem.objects.filter(cart=cart)

    total_price = 0

    for item in cartitems:

        total_price += item.product.price * item.quantity

    if request.method == "POST":

        name = request.POST.get('name')

        address = request.POST.get('address')

        phone = request.POST.get('phone')

        # RAZORPAY CLIENT

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        # CREATE RAZORPAY ORDER

        payment = client.order.create({

            "amount": int(total_price * 100),

            "currency": "INR",

            "payment_capture": 1
        })

        print("PAYMENT =>", payment)

        # CREATE ORDER

        order = Order()

        order.user = user

        order.name = name

        order.address = address

        order.phone_number = phone

        order.payment_method = "Razorpay"

        order.payment_status = "Pending"

        order.total_amount = total_price

        order.razorpay_order_id = payment['id']

        order.save()

        print("ORDER SAVED =>", order.razorpay_order_id)

        # CREATE ORDER ITEMS

        for item in cartitems:

            OrderItem.objects.create(

                order=order,

                product=item.product,

                quantity=item.quantity
            )

        context = {

            'payment': payment,

            'order': order,

            'total_price': total_price,

            'cartitems': cartitems,

            'razorpay_key': settings.RAZORPAY_KEY_ID
        }

        return render(
            request,
            'orders/payment.html',
            context
        )

    context = {

        'cartitems': cartitems,

        'total_price': total_price,

        'user': user
    }

    return render(
        request,
        'orders/orders_page.html',
        context
    )


def payment_success(request):

    razorpay_payment_id = request.GET.get(
        'razorpay_payment_id'
    )

    razorpay_order_id = request.GET.get(
        'razorpay_order_id'
    )

    razorpay_signature = request.GET.get(
        'razorpay_signature'
    )

    print("PAYMENT ID =>", razorpay_payment_id)

    print("ORDER ID =>", razorpay_order_id)

    print("SIGNATURE =>", razorpay_signature)

    try:

        # FIND ORDER

        order = Order.objects.get(
            razorpay_order_id=razorpay_order_id
        )

        print("ORDER FOUND =>", order.id)

        # SAVE PAYMENT DETAILS

        order.razorpay_payment_id = razorpay_payment_id

        order.razorpay_signature = razorpay_signature
        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        client.utility.verify_payment_signature(params_dict)

        order.payment_status = "Paid"

        order.save()

        print("PAYMENT SAVED")

        # CLEAR CART

        user = order.user

        cart = Cart.objects.get(user=user)

        cartitems = CartItem.objects.filter(cart=cart)

        cartitems.delete()

        print("CART CLEARED")

        return render(
            request,
            'orders/success.html'
        )

    except Exception as e:

        print("ERROR =>", e)

        return HttpResponse("Payment Failed")