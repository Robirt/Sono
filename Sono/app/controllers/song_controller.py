from django.shortcuts import render, redirect
from ..services.song_service import SongService
from ..services.album_service import AlbumService
from ..forms import SongForm

song_service: SongService = SongService()
album_service: AlbumService = AlbumService()

def songs(request):
    songs = song_service.get_songs();

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

    return render(request, 'app/songs/songs.html', {'songs': songs, 'form': form, 'albums': album_service.get_albums(), 'group': request.user.groups.first().name if request.user.groups.first() else None})