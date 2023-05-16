from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.band_service import BandService
from ..forms import BandForm
from ..models import Band

band_service: BandService = BandService()

def bands(request):
    bands = Band.objects.all()
    form = BandForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = BandForm(request.POST)
            if form.is_valid():
                band_service.add_band(form.save(commit=False))
                return redirect('bands')

        if 'update' in request.POST:
            form = BandForm(request.POST, instance = band_service.get_band_by_id(request.POST['id']))
            if form.is_valid():
                band_service.update_band(form.save(commit=False))
                return redirect('bands')

        elif 'delete' in request.POST:
            band_service.delete_band(request.POST['id'])
            return redirect('bands')

    return render(request, 'app/bands/bands.html', {'bands': bands, 'form': form})