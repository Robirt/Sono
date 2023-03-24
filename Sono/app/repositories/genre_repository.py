from django.db.models.query import QuerySet
from ..models import Genre

class GenreRepository():
    def get_genres(self) -> QuerySet[dict]:
        return Genre.object.all().values()

    def get_genre_by_id(self, id: int) -> Genre:
        return Genre.objects.get(id=id)

    def add_genre(self, genre: Genre) -> None:
        genre.save()

    def update_genre(self, genre: Genre) -> None:
        genre.save()

    def delete_genre(self, id: int) -> None:
        Genre.delete(Genre.objects.get(id=id))

