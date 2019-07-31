from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('Welcome to PyShop New Arrivals')

