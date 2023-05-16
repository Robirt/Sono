from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.rental_service import RentalService
from ..forms import RentalForm
from ..models import Rental

rental_service: RentalService = RentalService()

def rentals(request):
    rentals = Rental.objects.all()
    form = RentalForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = RentalForm(request.POST)
            if form.is_valid():
                rental_service.add_rental(form.save(commit=False))
                return redirect('rentals')

        if 'update' in request.POST:
            form = RentalForm(request.POST, instance = rental_service.get_rental_by_id(request.POST['id']))
            if form.is_valid():
                rental_service.update_rental(form.save(commit=False))
                return redirect('rentals')

        elif 'delete' in request.POST:
            rental_service.delete_rental(request.POST['id'])
            return redirect('rentals')

    return render(request, 'app/rentals/rentals.html', {'rentals': rentals, 'form': form})