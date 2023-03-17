from django.db.models.query import QuerySet
from ..models import Band

class BandRepository():
    def get_bands() -> QuerySet[dict]:
        return Band.object.all().values()

    def get_band_by_id(id: int) -> Band:
        return Band.objects.get(id=id)

    def add_band(band: Band) -> None:
        band.save()

    def update_band(band: Band) -> None:
        band.save()

    def delete_band(id: int) -> None:
        Band.delete(Band.objects.get(id=id))

