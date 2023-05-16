from django.db.models.query import QuerySet
from ..models import BandMember

class BandMemberRepository():
    def get_band_member() -> QuerySet[dict]:
        return BandMember.object.all().values()

    def get_band_member_by_id(self, id: int) -> BandMember:
        return BandMember.objects.get(id=id)

    def add_band_member(self, band_member: BandMember) -> None:
        band_member.save()

    def update_band_member(self, band_member: BandMember) -> None:
        band_member.save()

    def delete_band_member(self, band_member : BandMember) -> None:
        BandMember.delete(band_member)
