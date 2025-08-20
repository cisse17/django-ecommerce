from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from shop import settings

from .views import index, product_detail
from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path('', index, name='boutique'),
    path('product/<str:slug>/', product_detail, name='product_detail'),
    path("signup/", signup, name="signup"),
    path("logout/", logout_user, name="logout"),
    path("login_user/", login_user, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
