from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):

    product_list = Product.objects.all()
    return render(request, 'accounts/products.html',{'products' : product_list})


def customer(request):
    return render(request, 'accounts/curstomer.html')
