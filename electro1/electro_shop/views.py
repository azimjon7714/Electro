from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
import requests

def base_view(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'brands': brands,
        'products': products,
        'cart': cart
    }
    return render(request, 'index.html', context)

def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_by_category = Product.objects.filter(category=category)
    len_products = len(products_by_category)
    brands = Brand.objects.all()
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'category': category,
        'products_by_category': products_by_category,
        'len_products': len_products,
        'brands': brands,
        'cart': cart
    }
    return render(request, 'store.html', context)

def product_view(request, product_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    random_products = Product.objects.order_by('?')[:4]
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'product': product,
        'random_products': random_products,
        'cart': cart
    }
    return render(request, 'product.html', context)

def cart_view(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, 'checkout.html', context)

def add_to_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('cart')


def test_view(request):
    products = TestProduct.objects.all()
    context = {
        'products': products
    }
    return render(request, 'test.html', context)


def send_message(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    adress = request.POST.get('adress')
    message = 'Заявка с сайта : \nИмя - ' + str(name) + '\nТелефон - ' + str(phone)

    url = 'https://api.telegram.org/bot'
    token = '911064383:AAEk0L_fWOyuTK7PkJkoaLaSXtVOvmGzbqk'
    user_id = '898630999'
    url += token
    method = url + '/sendMessage'

    r = requests.post(method, data={
        'chat_id': user_id,
        'text': message
    })
    if r.status_code != 200:
        raise Exception("post_text erroe")

    return render(request, 'success.html')
