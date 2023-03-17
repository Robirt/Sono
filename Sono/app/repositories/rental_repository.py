from django.db.models.query import QuerySet
from ..models import Rental

class RentalRepository():
    def get_rentals() -> QuerySet[dict]:
        return Rental.object.all().values()

    def get_rental_by_id(id: int) -> Rental:
        return Rental.objects.get(id=id)

    def add_rental(rental: Rental) -> None:
        rental.save()

    def update_rental(rental: Rental) -> None:
        rental.save()

    def delete_rental(id: int) -> None:
        Rental.delete(Rental.objects.get(id=id))
