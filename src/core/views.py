from django.shortcuts import render

def front_page(request):
    return render(request,'core/frontpage.html',)

def contact(request):
    return render(request,'core/contact.html',)
