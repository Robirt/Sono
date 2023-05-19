from django.db.models.query import QuerySet
from ..models import Rental

class RentalRepository():
    def get_rentals(self) -> QuerySet[Rental]:
        return Rental.objects.all()

    def get_rental_by_id(self, id: int) -> Rental:
        return Rental.objects.get(id=id)

    def add_rental(self, rental: Rental) -> None:
        rental.save()

    def update_rental(self, rental: Rental) -> None:
        rental.save()

    def delete_rental(self, rental: Rental) -> None:
        Rental.delete(rental)
