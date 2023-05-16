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
        if 'add' in request.POST:
            form = SongForm(request.POST)
            if form.is_valid():
                song_service.add_song(form.save(commit=False))
                return redirect('songs')

        if 'update' in request.POST:
            form = SongForm(request.POST, instance = song_service.get_song_by_id(request.POST['id']))
            if form.is_valid():
                song_service.update_song(form.save(commit=False))
                return redirect('songs')

        elif 'delete' in request.POST:
            song_service.delete_song(request.POST['id'])
            return redirect('songs')

    return render(request, 'app/songs/songs.html', {'songs': songs, 'form': form})