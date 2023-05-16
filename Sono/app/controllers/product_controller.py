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
        if 'add' in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                product_service.add_product(form.save(commit=False))
                return redirect('products')

        if 'update' in request.POST:
            form = ProductForm(request.POST, instance = product_service.get_product_by_id(request.POST['id']))
            if form.is_valid():
                product_service.update_product(form.save(commit=False))
                return redirect('products')

        elif 'delete' in request.POST:
            product_service.delete_product(request.POST['id'])
            return redirect('products')

    return render(request, 'app/products/products.html', {'products': products, 'form': form})