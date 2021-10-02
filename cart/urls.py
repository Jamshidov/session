from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.index, name='homepage'),
    path('cart/', views.cart_page, name="cart_page"),
    # path('set/', views.setsession, name='set_session'),
    # path('get/', views.getsession, name='get_session'),
    # path('del/', views.delsession, name='del_session'),
    path('add', views.item_add, name='item_add'),
    path('decrement', views.item_decrement, name='item_decrement'),
    path('remove', views.remove, name='remove'),
    path('clear', views.cart_clear, name='cart_clear'),
]