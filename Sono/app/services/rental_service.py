from django.db.models.query import QuerySet
from ..repositories.rental_repository import RentalRepository
from ..models import Rental

class RentalService():
    def get_rentals(self) -> QuerySet[dict]:
        return RentalRepository.get_rentals()

    def get_rental_by_id(self, id: int) -> Rental:
        return RentalRepository.get_rental_by_id(id)

    def get_rental_by_title(self, title: str) -> Rental:
        return self.get_rentals().filter(title = title)
   
    def add_rental(self, rental: Rental) -> None:
        RentalRepository.add_rental(rental)
        
    def update_rental(self, rental: Rental) -> None:
        RentalRepository.update_rental(rental)

    def delete_rental(self, id: int) -> None:
        RentalRepository.delete_rental(self.get_rental_by_id(id))

