from django.db.models.query import QuerySet
from ..models import Album

class AlbumRepository():
    def get_albums():
        return list(Album.objects.all().prefetch_related('band'))

    def get_album_by_id(self, id: int) -> Album:
        return Album.objects.get(id=id)

    def add_album(self, album: Album) -> None:
        album.save()

    def update_album(self, album: Album) -> None:
        album.save()

    def delete_album(self, album: Album) -> None:
        Album.delete(album)
