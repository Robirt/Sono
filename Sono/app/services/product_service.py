from django.db.models.query import QuerySet
from ..repositories.product_repository import ProductRepository
from ..models import Product

class ProductService():
    def get_products(self) -> QuerySet[dict]:
        return ProductRepository.get_products()

    def get_product_by_id(self, id: int) -> Product:
        return ProductRepository.get_product_by_id(id)

    def get_product_by_code(self, code: str) -> Product:
        return ProductRepository.get_products().filter(code = code)
   
    def add_product(self, product: Product) -> None:
        ProductRepository.add_product(product)
        
    def update_product(self, product: Product) -> None:
        ProductRepository.update_product(product)

    def delete_product(self, id: int) -> None:
        ProductRepository.delete_product(self.get_product_by_id(id))
