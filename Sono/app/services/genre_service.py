from django.db.models.query import QuerySet
from ..repositories.genre_repository import GenreRepository
from ..models import Genre

class GenreService():
    def get_genres(self) -> QuerySet[dict]:
        return GenreRepository.get_genres()

    def get_genre_by_id(self, id: int) -> Genre:
        return GenreRepository.get_genre_by_id(id)

    def get_genre_by_name(self, name: str) -> Genre:
        return self.get_genres().filter(name = name)
   
    def add_genre(self, genre: Genre) -> None:
        GenreRepository.add_genre(genre)
        
    def update_genre(self, genre: Genre) -> None:
        GenreRepository.update_genre(genre)

    def delete_genre(self, id: int) -> None:
        GenreRepository.delete_genre(self.get_genre_by_id(id))
