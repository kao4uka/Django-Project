from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm


# Create your views here.

def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/main.html")


def products_view(request):
    if request.method == "GET":
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
            ],
            'user': request.user
        }

        return render(request, 'products/products.html', context=context)

def product_detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)

        context = {
            "product": product,
            "reviews": product.reviews.all(),
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == "POST":
        data = request.POST
        form = ReviewCreateForm(data=data)
        product = Product.objects.get(id=id)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )

        context = {
            'product': product,
            'review': product.reviews.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)

def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == "POST":
        data, files = request.POST, request.FILES

        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price')
            )

            return redirect('/products')

        return render(request, 'products/create.html', context={
            'form': form
        })