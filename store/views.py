from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)

def product_detail(request, slug):

    # product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'store/product_detail.html', {'product':product})