from django.db.models.query import QuerySet
from ..repositories.band_repository import BandRepository
from ..models import Band

class BandService():
    def get_bands(self):
        return BandRepository.get_bands()

    def search_bands_by_name(self, search_string: str) -> QuerySet[Band]:
        return BandRepository.get_bands().filter(name__icontains = search_string)

    def get_band_by_id(self, id: int) -> Band:
        return BandRepository.get_band_by_id(id)

    def get_band_by_title(self, title: str) -> Band:
        return self.get_bands().filter(title = title)
   
    def add_band(self, band: Band) -> None:
        BandRepository.add_band(band)
        
    def update_band(self, band: Band) -> None:
        BandRepository.update_band(band)

    def delete_band(self, id: int) -> None:
        BandRepository.delete_band(self.get_band_by_id(id))
