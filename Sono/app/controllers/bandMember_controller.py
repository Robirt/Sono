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
        if 'Update' in request.POST:
            bandMember_id = request.POST.get('bandMember_id')
            bandMember = BandMember.objects.get(id=bandMember_id)
            form = BandMemberForm(request.POST, instance=bandMember)
            if form.is_valid():
                form.save()
                return redirect('bandMembers')

        elif 'Remove' in request.POST:
            bandMember_id = request.POST.get('bandMember_id')
            bandMember = BandMember.objects.get(id=bandMember_id)
            bandMember.delete()
            return redirect('bandMembers')

        elif 'Add' in request.POST:
            form = BandMemberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('bandMembers')

    return render(request, 'app/bandMembers/bandMembers.html', {'bandMembers': bandMembers, 'form': form})