from src.data_access.models.models import Product
from src.data_access.repositories import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def find_by_id(self, product_id: int) -> Product:
        return self.repo.find_by_id(product_id)

    def find_all_pageable(self, page, rows_per_page: int = 5):
        return self.repo.find_all_pageable(page, rows_per_page)
