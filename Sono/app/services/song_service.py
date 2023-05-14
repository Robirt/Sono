from django.db.models.query import QuerySet
from ..repositories.song_repository import SongRepository
from ..models import Song

class SongService():
    def get_songs(self) -> QuerySet[dict]:
        return SongRepository.get_songs()

    def get_song_by_id(self, id: int) -> Song:
        return SongRepository.get_song_by_id(id)

    def get_song_by_title(self, title: str) -> Song:
        return self.get_songs().filter(title = title)
   
    def add_song(self, song) -> None:
        SongRepository.add_song(song)
        
    def update_song(self, song: Song) -> None:
        SongRepository.update_song(song)

    def delete_song(self, id: int) -> None:
        SongRepository.delete_song(self.get_song_by_id(id))
