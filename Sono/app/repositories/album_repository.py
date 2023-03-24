from django.db.models.query import QuerySet
from ..models import Album

class AlbumRepository():
    def get_albums() -> QuerySet[dict]:
        return Album.object.all().values()

    def get_album_by_id(id: int) -> Album:
        return Album.objects.get(id=id)

    def add_album(album: Album) -> None:
        album.save()

    def update_album(album: Album) -> None:
        album.save()

    def delete_album(id: int) -> None:
        Album.delete(Album.objects.get(id=id))
