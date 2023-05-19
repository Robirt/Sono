from django.shortcuts import render, redirect
from ..services.product_service import ProductService
from ..services.album_service import AlbumService
from ..forms import ProductForm

product_service: ProductService = ProductService()
album_service: AlbumService = AlbumService()

def products(request):
    if request.user.groups.first().name == 'Users':
        return redirect('home')

    products = product_service.get_products()

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

    return render(request, 'app/products/products.html', {'products': products, 'form': form, 'albums': album_service.get_albums(), 'group': request.user.groups.first().name if request.user.groups.first() else None})

def history(request):
    if request.user.groups.first().name == 'Administrator':
        return redirect('home')

    products = product_service.get_products().filter(rental__renter=request.user).select_related('rental__renter', 'album')

    return render(request, 'app/rentals/history.html', {'products': products, 'group': request.user.groups.first().name if request.user.groups.first() else None})