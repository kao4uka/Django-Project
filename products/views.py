from django.shortcuts import render
from products.models import Product

# Create your views here.

def main_view(requests):
    if requests.method == "GET":
        return render(requests, "layouts/main.html")

def products_view(requests):
    if requests.method == "GET":
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(requests, 'products/products.html', context=context)