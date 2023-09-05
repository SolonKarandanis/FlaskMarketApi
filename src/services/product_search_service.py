from celery import shared_task

from src.data_access.models.models import Product
from src.data_access.repositories import ProductRepository


class ProductSearchService:

    def __init__(self, repo: ProductRepository):
        self.repo = repo

    # @shared_task
    def add_to_product_index(self) -> None:
        objects_to_be_indexed = self.repo.find_all()
        Product.reindex(objects_to_be_indexed)

    def remove_from_product_index(self, index, model):
        pass

    def query_product_index(self, query, page, per_page):
        return Product.search(query, page, per_page)
