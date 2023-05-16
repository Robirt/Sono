from django.db.models.query import QuerySet
from ..repositories.band_repository import BandRepository
from ..models import Band

class BandService():
    def __init__(self) -> None:
        self.band_repository = BandRepository()

    def get_bands(self) -> QuerySet[dict]:
        return self.band_repository.get_bands()

    def get_band_by_id(self, id: int) -> Band:
        return self.band_repository.get_band_by_id(id)

    def get_band_by_name(self, name: str) -> Band:
        return self.get_bands().filter(name=name)

    def add_band(self, band: Band) -> None:
        self.band_repository.add_band(band)

    def update_band(self, band: Band) -> None:
        self.band_repository.update_band(band)

    def delete_band(self, id: int) -> None:
        self.band_repository.delete_band(self.get_band_by_id(id))
