from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.bandMember_service import BandMemberService
from ..forms import BandMemberForm
from ..models import BandMember

bandMember_service: BandMemberService = BandMemberService()

def bandMembers(request):
    bandMembers = BandMember.objects.all()
    form = BandMemberForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = BandMemberForm(request.POST)
            if form.is_valid():
                bandMember_service.add_bandMember(form.save(commit=False))
                return redirect('bandMembers')

        if 'update' in request.POST:
            form = BandMemberForm(request.POST, instance = bandMember_service.get_bandMember_by_id(request.POST['id']))
            if form.is_valid():
                bandMember_service.update_bandMember(form.save(commit=False))
                return redirect('bandMembers')

        elif 'delete' in request.POST:
            bandMember_service.delete_bandMember(request.POST['id'])
            return redirect('bandMembers')

    return render(request, 'app/bandMembers/bandMembers.html', {'bandMembers': bandMembers, 'form': form})