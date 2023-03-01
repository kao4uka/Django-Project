from django.contrib import admin
from django.urls import path
from products.views import main_view, products_view, product_detail_view, create_product_view
from django.conf.urls.static import static
from Blog import settings
from users.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', create_product_view),

    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
