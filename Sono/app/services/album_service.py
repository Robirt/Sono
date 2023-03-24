from django.db.models.query import QuerySet
from ..repositories.album_repository import AlbumRepository
from ..models import Album

class AlbumService():
    def get_albums(self) -> QuerySet[dict]:
        return AlbumRepository.get_albums()

    def search_albums_by_title(self, search_string: str) -> QuerySet[Album]:
        return AlbumRepository.get_Albums().filter(title__icontains = search_string)

    def get_album_by_id(self, id: int) -> Album:
        return AlbumRepository.get_album_by_id(id)

    def get_album_by_title(self, title: str) -> Album:
        return self.get_albums().filter(title = title)
   
    def add_album(self, album: Album) -> None:
        AlbumRepository.add_album(album)
        
    def update_album(self, album: Album) -> None:
        AlbumRepository.update_album(album)

    def delete_album(self, id: int) -> None:
        AlbumRepository.delete_album(self.get_album_by_id(id))

