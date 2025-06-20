from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
def buy_now(request, pk):
    product = get_object_or_404(Product, pk=pk)
    success = False

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        payment = request.POST.get('payment')
        # Normally store order in DB here
        success = True

    return render(request, 'buy_now.html', {'product': product, 'success': success})