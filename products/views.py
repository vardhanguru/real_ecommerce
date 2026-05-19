from django.shortcuts import render

# Create your views here.

from .models import Products

def all_products(request):
    products = Products.objects.all()
    print(request.session.get('id'))
    for product in products:
        product.image = str(product.image)[13:]
    data = {'products': products}

    return render(request, 'base.html', context=data)


def product_details(request, id):
    product_details = Products.objects.get(id=id)
    product_details.image = str(product_details.image)[13:]
    data = {'product':product_details}

    return render(request, 'products/product_detail.html', context = data)