from django.db.models.query import QuerySet
from ..models import Genre

class GenreRepository():
    def get_genres() -> QuerySet[dict]:
        return Genre.object.all().values()

    def get_genre_by_id(id: int) -> Genre:
        return Genre.objects.get(id=id)

    def add_genre(genre: Genre) -> None:
        genre.save()

    def update_genre(genre: Genre) -> None:
        genre.save()

    def delete_genre(id: int) -> None:
        Genre.delete(Genre.objects.get(id=id))

