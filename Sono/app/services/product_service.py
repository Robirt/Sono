from django.db.models.query import QuerySet
from ..repositories.product_repository import ProductRepository
from ..models import Product

class ProductService():
    def __init__(self) -> None:
        self.product_repository = ProductRepository()

    def get_products(self) -> QuerySet[dict]:
        return self.product_repository.get_products()

    def get_product_by_id(self, id: int) -> Product:
        return self.product_repository.get_product_by_id(id)

    def get_product_by_name(self, name: str) -> Product:
        return self.get_products().filter(name=name)

    def add_product(self, product: Product) -> None:
        self.product_repository.add_product(product)

    def update_product(self, product: Product) -> None:
        self.product_repository.update_product(product)

    def delete_product(self, id: int) -> None:
        self.product_repository.delete_product(self.get_product_by_id(id))
