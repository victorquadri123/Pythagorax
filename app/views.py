from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def landing(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def create_account(request):
    return render(request, 'create-account.html')



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def single_product(request):
    return render(request, 'single-product.html')

def all_product(request):
    return render( request, 'all-product.html')
