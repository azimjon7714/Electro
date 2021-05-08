from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', base_view, name='base'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    path('test', test_view, name='test'),
    path('cart', cart_view, name='cart'),
    path('send_message', send_message, name='send_message'),
    re_path(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', add_to_cart_view, name='add_to_cart'),

]
