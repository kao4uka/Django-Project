from django.contrib import admin
from django.urls import path
from products.views import main_view, products_view
from django.conf.urls.static import static
from Blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)