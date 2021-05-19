from django.shortcuts import render
from product.models import Product

def front_page(request):
    newest_products = Product.objects.all()[0:8]
    return render(request,'core/front_page.html',{'newest_products':newest_products})

def contact(request):
    return render(request,'core/contact.html',)
