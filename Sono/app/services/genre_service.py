from django.db.models.query import QuerySet
from ..repositories.genre_repository import GenreRepository
from ..models import Genre

class GenreService:
    def __init__(self) -> None:
        self.genre_repository = GenreRepository()

    def get_genres(self) -> QuerySet[dict]:
        return self.genre_repository.get_genres()

    def get_genre_by_id(self, id: int) -> Genre:
        return self.genre_repository.get_genre_by_id(id)

    def get_genre_by_name(self, name: str) -> Genre:
        return self.get_genres().filter(name=name)

    def add_genre(self, genre: Genre) -> None:
        self.genre_repository.add_genre(genre)

    def update_genre(self, genre: Genre) -> None:
        self.genre_repository.update_genre(genre)

    def delete_genre(self, id: int) -> None:
        self.genre_repository.delete_genre(self.get_genre_by_id(id))
