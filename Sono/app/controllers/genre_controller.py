from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..services.genre_service import GenreService
from ..forms import GenreForm
from ..models import Genre

genre_service: GenreService = GenreService()

def genres(request):
    genres = Genre.objects.all()
    form = GenreForm()

    if request.method == 'POST':
        if 'Update' in request.POST:
            genre_id = request.POST.get('genre_id')
            genre = Genre.objects.get(id=genre_id)
            form = GenreForm(request.POST, instance=genre)
            if form.is_valid():
                form.save()
                return redirect('genres')

        elif 'Remove' in request.POST:
            genre_id = request.POST.get('genre_id')
            genre = Genre.objects.get(id=genre_id)
            genre.delete()
            return redirect('genres')

        elif 'add_genre' in request.POST:
            form = GenreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('genres')

    return render(request, 'app/genres/genres.html', {'genres': genres, 'form': form})

