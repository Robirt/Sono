from django.db.models.query import QuerySet
from ..models import Band

class BandRepository():
    def get_bands(self) -> QuerySet[Band]:
        return Band.objects.all()

    def get_band_by_id(self, id: int) -> Band:
        return Band.objects.get(id=id)

    def add_band(self, band: Band) -> None:
        band.save()

    def update_band(self, band: Band) -> None:
        band.save()

    def delete_band(self, band: Band) -> None:
        Band.delete(band)

