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
        if 'update' in request.POST:
            band_id = request.POST.get('id')
            band = Band.objects.get(id=band_id)
            form = BandForm(request.POST, request.FILES, instance=band)
            if form.is_valid():
                form.save()
                return redirect('bands')

        elif 'delete' in request.POST:
            band_id = request.POST.get('id')
            band = Band.objects.get(id=band_id)
            band.delete()
            return redirect('bands')

        elif 'add' in request.POST:
            form = BandForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('bands')

    return render(request, 'app/bands/bands.html', {'bands': bands, 'form': form})