import random
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import  render, get_object_or_404, redirect
from .models import *

from .cart import Cart
from .forms import AddToCartForm

RANDOM_PRODUCT = 4

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            messages.success(request, 'The product was added to the cart')

            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    return render(request, 'product/search.html', {\
                            'form':form,\
                            'products': products,\
                            'query': query})

def product(request, category_slug, product_slug):
    cart = Cart(request)
    print(22, vars(cart))
    product = get_object_or_404(Product,  slug = product_slug)
    similiar_products = list(product.category.products.exclude(id=product.id))
    print(25, category_slug)
    if len(similiar_products)>=RANDOM_PRODUCT:
        similiar_products = random.sample(similiar_products,4)

    return render(request, 'product/product.html',{'product':product, \
                                                   'similiar_products':similiar_products})

def category(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category':category})
