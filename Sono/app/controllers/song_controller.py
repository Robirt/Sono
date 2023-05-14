from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.song_service import SongService
from ..forms import SongForm
from ..models import Song

song_service: SongService = SongService()

def songs(request):
    songs = Song.objects.all()
    form = SongForm()

    if request.method == 'POST':
        if 'Update' in request.POST:
            song_id = request.POST.get('song_id')
            song = Song.objects.get(id=song_id)
            form = SongForm(request.POST, instance=song)
            if form.is_valid():
                form.save()
                return redirect('songs')

        elif 'Remove' in request.POST:
            song_id = request.POST.get('song_id')
            song = Song.objects.get(id=song_id)
            song.delete()
            return redirect('songs')

        elif 'Add' in request.POST:
            form = SongForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('songs')

    return render(request, 'app/songs/songs.html', {'songs': songs, 'form': form})