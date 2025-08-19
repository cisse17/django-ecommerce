from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from shop import settings

from .views import index, product_detail

urlpatterns = [
    path('', index, name='boutique'),
    path('product/<str:slug>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
