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
        if 'add' in request.POST:
            form = AlbumForm(request.POST)
            if form.is_valid():
                album_service.add_album(form.save(commit=False))
                return redirect('albums')

        if 'update' in request.POST:
            form = AlbumForm(request.POST, instance = album_service.get_album_by_id(request.POST['id']))
            if form.is_valid():
                album_service.update_album(form.save(commit=False))
                return redirect('albums')

        elif 'delete' in request.POST:
            album_service.delete_album(request.POST['id'])
            return redirect('albums')

    return render(request, 'app/albums/albums.html', {'albums': albums, 'form': form})

