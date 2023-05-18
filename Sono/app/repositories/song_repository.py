from django.db.models.query import QuerySet
from ..models import Song

class SongRepository():
    def get_songs(self) -> QuerySet[dict]:
        return Song.objects.all()

    def get_song_by_id(self, id: int) -> Song:
        return Song.objects.get(id=id)

    def add_song(self, song: Song) -> None:
        song.save()

    def update_song(self, song: Song) -> None:
        song.save()

    def delete_song(self, song: Song) -> None:
        Song.delete(song)

