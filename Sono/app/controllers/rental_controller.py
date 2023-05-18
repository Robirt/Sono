from django.shortcuts import render, redirect
from ..services.rental_service import RentalService
from ..forms import RentalForm

rental_service: RentalService = RentalService()

def rentals(request):
    rentals = rental_service.get_rentals()

    form = RentalForm()

    if request.method == 'POST':
        if 'delete' in request.POST:
            rental_service.delete_rental(request.POST['id'])
            return redirect('rentals')

    return render(request, 'app/rentals/rentals.html', {'rentals': rentals, 'form': form})