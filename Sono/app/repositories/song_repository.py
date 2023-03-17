from django.db.models.query import QuerySet
from ..models import Song

class SongRepository():
    def get_songs() -> QuerySet[dict]:
        return Song.object.all().values()

    def get_song_by_id(id: int) -> Song:
        return Song.objects.get(id=id)

    def add_song(song: Song) -> None:
        song.save()

    def update_song(song: Song) -> None:
        song.save()

    def delete_song(id: int) -> None:
        Song.delete(Song.objects.get(id=id))

