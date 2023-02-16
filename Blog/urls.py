from django.contrib import admin
from django.urls import path
from products.views import main_view, products_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view)
]
