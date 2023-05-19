from django.shortcuts import render, redirect
from ..services.band_member_service import BandMemberService
from ..services.band_service import BandService
from ..forms import BandMemberForm

band_member_service: BandMemberService = BandMemberService()
bands_service: BandService = BandService()

def band_members(request):
    band_members = band_member_service.get_band_members()

    form = BandMemberForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = BandMemberForm(request.POST)
            if form.is_valid():
                band_member_service.add_band_member(form.save(commit=False))
                return redirect('band_members')

        if 'update' in request.POST:
            form = BandMemberForm(request.POST, instance = band_member_service.get_band_member_by_id(request.POST['id']))
            if form.is_valid():
                band_member_service.update_band_member(form.save(commit=False))
                return redirect('band_members')

        elif 'delete' in request.POST:
            band_member_service.delete_band_member(request.POST['id'])
            return redirect('band_members')

    return render(request, 'app/band_members/band_members.html', {'band_members': band_members, 'form': form, 'bands': bands_service.get_bands(), 'group': request.user.groups.first().name if request.user.groups.first() else None})