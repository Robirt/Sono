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
        if 'Update' in request.POST:
            rental_id = request.POST.get('rental_id')
            rental = Rental.objects.get(id=rental_id)
            form = RentalForm(request.POST, instance=rental)
            if form.is_valid():
                form.save()
                return redirect('rentals')

        elif 'Remove' in request.POST:
            rental_id = request.POST.get('rental_id')
            rental = Rental.objects.get(id=rental_id)
            rental.delete()
            return redirect('rentals')

        elif 'Add' in request.POST:
            form = RentalForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('rentals')

    return render(request, 'app/rentals/rentals.html', {'rentals': rentals, 'form': form})