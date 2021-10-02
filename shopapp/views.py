from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .cart import Cart


def index(request):
    products = Product.objects.all()
    return render(request, 'shopapp/dist/index.html', {"products": products})


def add_page(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("shopapp:home")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("shopapp:on-cart")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("shopapp:on-cart")


def remove(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("shopapp:on-cart")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("shopapp:home")


def cart(request):
    cart = Cart(request)
    items = cart.items()
    total_price = cart.get_total_price()
    count = cart.get_total_items()

    context = {
        "items": items,
        "count": count,
        "total_price": total_price,
    }
    return render(request, 'shopapp/dist/cart.html', context)
