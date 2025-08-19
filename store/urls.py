from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from shop import settings

from .views import index

urlpatterns = [
    path('', index, name='boutique')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
