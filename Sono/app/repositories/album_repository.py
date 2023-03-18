from django.db.models.query import QuerySet
from ..models import Album

class AlbumRepository():
    def get_Albums() -> QuerySet[dict]:
        return Album.object.all().values()

    def get_Album_by_id(id: int) -> Album:
        return Album.objects.get(id=id)

    def add_Album(album: Album) -> None:
        album.save()

    def update_Album(album: Album) -> None:
        album.save()

    def delete_Album(id: int) -> None:
        Album.delete(Album.objects.get(id=id))
