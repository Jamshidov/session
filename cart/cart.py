from django.conf import settings
from decimal import Decimal
from django.shortcuts import redirect, render


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self):
        my_name = "jamshid"
        if my_name not in self.cart.values():
            self.cart = {"name": "jamshid", "age": 28}
        else:
            self.cart['age'] = self.cart['age'] + 1
        self.save()

    def decrement(self):
        my_name = "jamshid"
        if my_name in self.cart.values():
            self.cart['age'] = self.cart['age'] - 1
            if self.cart['age'] < 1:
                return redirect("homepage")
        else:
            return self.cart
        self.save()

    def remove(self):
        del self.cart['name']
        del self.cart['age']
        self.save()
        return redirect("cart:cart_page")

    def items(self):
        cart = self.cart.copy()
        return cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def cart_clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


