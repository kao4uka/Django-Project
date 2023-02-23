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
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'image': product.image,
                    'hashtags': product.hashtags.all()
                }
                for product in products
            ]
        }

        return render(requests, 'products/products.html', context=context)

def product_detail_view(requests, id):
    if requests.method == "GET":
        product = Product.objects.get(id=id)

        context = {
            "product": product,
            "reviews": product.reviews.all()
        }

        return render(requests, 'products/detail.html', context=context)