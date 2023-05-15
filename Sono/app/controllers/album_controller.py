from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.album_service import AlbumService
from ..forms import AlbumForm
from ..models import Album

album_service: AlbumService = AlbumService()

def albums(request):
    albums = Album.objects.all()
    form = AlbumForm()

    if request.method == 'POST':
        if 'Update' in request.POST:
            album_id = request.POST.get('album_id')
            album = Album.objects.get(id=album_id)
            form = AlbumForm(request.POST, instance=album)
            if form.is_valid():
                form.save()
                return redirect('albums')

        elif 'Remove' in request.POST:
            album_id = request.POST.get('album_id')
            album = Album.objects.get(id=album_id)
            album.delete()
            return redirect('albums')

        elif 'add_album' in request.POST:
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('albums')

    return render(request, 'app/albums/albums.html', {'albums': albums, 'form': form})

