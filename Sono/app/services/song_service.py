from django.db.models.query import QuerySet
from ..repositories.song_repository import SongRepository
from ..models import Song

class SongService():
    def __init__(self) -> None:
        self.song_repository = SongRepository()

    def get_songs(self) -> QuerySet[dict]:
        return self.song_repository.get_songs()

    def get_song_by_id(self, id: int) -> Song:
        return self.song_repository.get_song_by_id(id)

    def get_song_by_name(self, name: str) -> Song:
        return self.get_songs().filter(name=name)

    def add_song(self, song: Song) -> None:
        self.song_repository.add_song(song)

    def update_song(self, song: Song) -> None:
        self.song_repository.update_song(song)

    def delete_song(self, id: int) -> None:
        self.song_repository.delete_song(self.get_song_by_id(id))
