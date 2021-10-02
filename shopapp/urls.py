from django.urls import path
from .views import *

app_name = "shopapp"

urlpatterns = [
    path('', index, name="home"),
    path('on-cart', cart, name="on-cart"),

    path('item_add/<int:id>', add_page, name='item_add'),
    path('item_increment/<int:id>', item_increment, name='item_increment'),
    path('item_decrement/<int:id>', item_decrement, name='item_decrement'),
    path('item_remove/<int:id>', remove, name='item_remove'),
    path('cart_clear', cart_clear, name='cart_clear'),
]
