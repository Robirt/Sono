from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.genre_service import GenreService
from ..forms import GenreForm
from ..models import Genre

genre_service: GenreService = GenreService()

def genres(request):
    genres = genre_service.get_genres()

    form = GenreForm()

    if request.method == 'POST':
        if 'add' in request.POST:
            form = GenreForm(request.POST)
            if form.is_valid():
                genre_service.add_genre(form.save(commit=False))
                return redirect('genres')

        if 'update' in request.POST:
            form = GenreForm(request.POST, instance = genre_service.get_genre_by_id(request.POST['id']))
            if form.is_valid():
                genre_service.update_genre(form.save(commit=False))
                return redirect('genres')

        elif 'delete' in request.POST:
            genre_service.delete_genre(request.POST['id'])
            return redirect('genres')

    return render(request, 'app/genres/genres.html', {'genres': genres, 'form': form})

