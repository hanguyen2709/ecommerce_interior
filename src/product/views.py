import random

from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import  render, get_object_or_404
from .models import *

RANDOM_PRODUCT = 4


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})

def product(request, category_slug, product_slug):
    print(11, category_slug,product_slug)
    product = get_object_or_404(Product,  slug = product_slug)
    similiar_products = list(product.category.products.exclude(id=product.id))
    print(12, category_slug)
    if len(similiar_products)>=RANDOM_PRODUCT:
        similiar_products = random.sample(similiar_products,4)

    return render(request, 'product/product.html',{'product':product, \
                                                   'similiar_products':similiar_products})

def category(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category':category})
