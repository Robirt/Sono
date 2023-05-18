from django.db.models.query import QuerySet
from ..repositories.band_member_repository import BandMemberRepository
from ..models import Band

class BandMemberService():
    def __init__(self) -> None:
        self.band_member_repository = BandMemberRepository()

    def get_band_members(self) -> QuerySet[dict]:
        return self.band_member_repository.get_band_members()

    def get_band_member_by_id(self, id: int) -> Band:
        return self.band_member_repository.get_band_member_by_id(id)

    def add_band_member(self, band_member: Band) -> None:
        self.band_member_repository.add_band_member(band_member)

    def update_band_member(self, band_member: Band) -> None:
        self.band_member_repository.update_band_member(band_member)

    def delete_band_member(self, id: int) -> None:
        self.band_member_repository.delete_band_member(self.get_band_member_by_id(id))
