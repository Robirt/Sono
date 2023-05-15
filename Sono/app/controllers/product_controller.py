from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.product_service import ProductService
from ..forms import ProductForm
from ..models import Product

product_service: ProductService = ProductService()

def products(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        if 'Update' in request.POST:
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('products')

        elif 'Remove' in request.POST:
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            product.delete()
            return redirect('products')

        elif 'Add' in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products')

    return render(request, 'app/products/products.html', {'products': products, 'form': form})