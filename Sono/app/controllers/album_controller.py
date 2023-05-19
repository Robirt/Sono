from django.shortcuts import render, redirect
from ..services.album_service import AlbumService
from ..services.band_service import BandService
from ..forms import AlbumForm
from ..models import Product

album_service: AlbumService = AlbumService()
band_service: BandService = BandService()

def albums(request):
    if request.user.groups.first().name == 'Users':
        return redirect('home')

    albums = album_service.get_albums()

    form = AlbumForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = AlbumForm(request.POST, request.FILES)
            if form.is_valid():
                album_service.add_album(form.save(commit=False))
                return redirect('albums')

        elif 'update' in request.POST:
            form = AlbumForm(request.POST, request.FILES, instance = album_service.get_album_by_id(request.POST['id']))
            if form.is_valid():
                album_service.update_album(form.save(commit=False))
                return redirect('albums')

        elif 'delete' in request.POST:
            album_service.delete_album(request.POST['id'])
            return redirect('albums')

    return render(request, 'app/albums/albums.html', {'albums': albums, 'form': form, 'bands': band_service.get_bands(), 'group': request.user.groups.first().name if request.user.groups.first() else None})

def album(request, title):
    if request.user.groups.first().name == 'Administrator':
        return redirect('home')
        
    album = album_service.get_album_by_title(title);
    songs = album.song_set.all()
    products = album.product_set.filter(rental__isnull=True)

    return render(request, 'app/albums/album.html', {'album': album, 'songs': songs, 'products': products, 'group': request.user.groups.first().name if request.user.groups.first() else None})