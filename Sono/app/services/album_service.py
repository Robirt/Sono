from django.db.models.query import QuerySet
from ..repositories.album_repository import AlbumRepository
from ..models import Album

class AlbumService():
    def __init__(self) -> None:
        self.album_repository = AlbumRepository()

    def get_albums(self) -> QuerySet[dict]:
        return self.album_repository.get_albums()

    def get_album_by_id(self, id: int) -> Album:
        return self.album_repository.get_album_by_id(id)

    def get_album_by_name(self, name: str) -> Album:
        return self.get_albums().filter(name=name)

    def add_album(self, album: Album) -> None:
        self.album_repository.add_album(album)

    def update_album(self, album: Album) -> None:
        self.album_repository.update_album(album)

    def delete_album(self, id: int) -> None:
        self.album_repository.delete_album(self.get_album_by_id(id))

