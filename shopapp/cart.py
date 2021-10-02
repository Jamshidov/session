from decimal import Decimal
from django.conf import settings
from .models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        ids = self.cart.keys()
        # products = Product.objects.filter(id__in=ids)

    def add(self, product, quantity=1):
        id = product.id
        if str(id) not in self.cart.keys():
            self.cart[id] = {
                "id": id,
                "name": product.name,
                "quantity": 1,
                "price": product.price,
            }
            print("no" + str(id))
        else:
            # print("yes" + str(id))
            for key, value in self.cart.items():
                if key == str(id):
                    value['quantity'] = value['quantity'] + 1
                # print(value['quantity'])
        self.save()
        # print(self.cart)

    def decrement(self, product):
        id = product.id
        needProducts = self.cart.values()
        for item in needProducts:
            if item['id'] == id:
                item['quantity'] = item['quantity'] - 1
                # print(item['quantity'])
                if item['quantity'] == 0:
                    return
        self.save()

    def remove(self, product):
        id = product.id
        for x, y in self.cart.items():
            if id == y['id']:
                key = x
        if key in self.cart:
            del self.cart[key]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        # self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def items(self):
        cart = self.cart.values()
        return cart

    def get_total_items(self):
        keys = self.cart.keys()
        count = len(keys)
        return count

    def get_total_price(self):
        a = []
        for item in self.cart.values():
            total_sum = item['quantity'] * Decimal(item['price'])
            a.append(total_sum)
        return sum(a)





