from django.db.models.query import QuerySet
from ..models import Product

class ProductRepository():
    def get_products() -> QuerySet[dict]:
        return Product.object.all().values()

    def get_product_by_id(self, id: int) -> Product:
        return Product.objects.get(id=id)

    def add_product(self, product: Product) -> None:
        product.save()

    def update_product(self, product: Product) -> None:
        product.save()

    def delete_product(self, product: Product) -> None:
        Product.delete(product)

