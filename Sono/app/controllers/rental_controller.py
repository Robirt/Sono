from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from ..services.rental_service import RentalService
from ..services.album_service import AlbumService
from ..services.product_service import ProductService
from ..models import Rental
from ..forms import RentalForm

rental_service: RentalService = RentalService()
album_serivce: AlbumService = AlbumService()
product_service: ProductService = ProductService()

def rentals(request):
    rentals = rental_service.get_rentals()

    form = RentalForm()

    if request.method == 'POST':
        if 'delete' in request.POST:
            rental_service.delete_rental(request.POST['id'])
            return redirect('rentals')

    return render(request, 'app/rentals/rentals.html', {'rentals': rentals, 'form': form, 'group': request.user.groups.first().name if request.user.groups.first() else None})

def rent(request, id: int):
    if request.user.groups.first().name == 'Administrator':
        return redirect('home')

    album = album_serivce.get_album_by_id(id)
    product = album.product_set.filter(rental__isnull=True).first();

    rental: Rental = Rental()
    rental.reservation_date = datetime.now() 
    rental.reservation_expire_date = datetime.now() + timedelta(days=7)
    rental.return_date = datetime.now() + timedelta(days=14)
    rental.renter = request.user
    rental_service.add_rental(rental)

    product.rental = rental

    product_service.update_product(product);

    return redirect('history')