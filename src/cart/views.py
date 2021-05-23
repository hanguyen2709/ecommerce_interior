# import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CheckoutForm
# import sys, os
# sys.path.insert(0, os.path.abspath('..'))
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)
    print(18,vars(cart),quantity)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request,'cart/cart.html')
