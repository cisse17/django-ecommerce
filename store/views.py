from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Cart, Order, Product
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

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user) # _  c'est une variable definie masi qui ne sera pas utilisé
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()

    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("product_detail", kwargs={"slug": slug}))
