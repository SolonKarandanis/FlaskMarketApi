from typing import List

from celery import shared_task

from src.data_access.models.models import Product
from src.data_access.repositories import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def find_by_id(self, product_id: int) -> Product:
        return self.repo.find_by_id(product_id)

    def find_all_pageable(self, page, rows_per_page: int = 5):
        return self.repo.find_all_pageable(page, rows_per_page)

    def find_by_ids(self, product_ids: List[int]) -> List[Product]:
        return self.repo.find_by_ids(product_ids)

    def find_all(self) -> List[Product]:
        return self.repo.find_all()

    @shared_task
    def schedule_index_products(self):
        products = self.find_all()