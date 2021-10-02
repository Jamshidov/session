from django.shortcuts import render, redirect
from django.conf import settings
from .cart import Cart


def index(request):
    return render(request, 'cart/index.html')


def item_add(request):
    cart = Cart(request)
    cart.add()
    return redirect("cart:cart_page")


def item_decrement(request):
    cart = Cart(request)
    cart.decrement()
    return redirect("cart:cart_page")


def remove(request):
    cart = Cart(request)
    cart.remove()
    return redirect("cart:cart_page")


def cart_clear(request):
    cart = Cart(request)
    cart.cart_clear()
    return redirect("cart:homepage")


def cart_page(request):
    cart = Cart(request)
    item = cart.items()
    return render(request, 'cart/cart.html', {"item": item})



























# def item_add(request):
#     cart = request.session.get(settings.CART_SESSION_ID)
#     if not cart:
#         cart = request.session[settings.CART_SESSION_ID] = {}
#     print(cart)
#     cart = {
#         "name": "jamshid",
#         "age": 28,
#     }
#     print(cart['age'])
#     for key, values in cart.items():
#         if "jamshid" == values:
#             cart['age'] += 1
#             print(cart)
#     return redirect("cart_page")



# def setsession(request):
#     request.session['name'] = "jamshid"
#     request.session['sname'] = "azizov"
#     return render(request, 'cart/index.html')
#
#
# def getsession(request):
#     # name = request.session['name']
#     name = request.session.get('name', default="you name")
#     sname = request.session.get('sname', default="you surname")
#     keys = request.session.keys()
#     items = request.session.items()
#     age = request.session.setdefault('age', '28')
#     context = {
#         "name": name,
#         "sname": sname,
#         "keys": keys,
#         "items": items,
#         "age": age,
#     }
#     return render(request, 'cart/index.html', context)
#
#
# def delsession(request):
#     # if 'name' and 'sname' in request.session:
#     #     del request.session['name']
#     #     del request.session['sname']
#     # request.session.flush()
#     # request.session.clear()
#     del request.session
#     return render(request, 'cart/index.html')































