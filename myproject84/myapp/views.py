from django.shortcuts import render, redirect
from .models import Product, Cart, Order
from .forms import OrderForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

def checkout(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.cart_items.set(Cart.objects.all())  # Link all cart items
            Cart.objects.all().delete()  # Clear cart after checkout
            return redirect('home')

    return render(request, 'checkout.html', {'form': form})
