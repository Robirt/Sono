from django.db.models.query import QuerySet
from ..repositories.rental_repository import RentalRepository
from ..models import Rental

class RentalService():
    def __init__(self) -> None:
        self.rental_repository = RentalRepository()

    def get_rentals(self) -> QuerySet[dict]:
        return self.rental_repository.get_rentals()

    def get_rental_by_id(self, id: int) -> Rental:
        return self.rental_repository.get_rental_by_id(id)

    def get_rental_by_name(self, name: str) -> Rental:
        return self.get_rentals().filter(name=name)

    def add_rental(self, rental: Rental) -> None:
        self.rental_repository.add_rental(rental)

    def update_rental(self, rental: Rental) -> None:
        self.rental_repository.update_rental(rental)

    def delete_rental(self, id: int) -> None:
        self.rental_repository.delete_rental(self.get_rental_by_id(id))

