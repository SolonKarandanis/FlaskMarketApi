from typing import List

from src.data_access.models.models import Product
from src.data_access.repositories.IRepository import IRepository


class ProductRepository(IRepository):
    def __init__(self, db):
        self.db = db

    def find_by_id(self, product_id: int) -> Product:
        return self.db.session.query(Product)\
            .options(self.db.joinedload(Product.types)).filter_by(id=product_id).first()

    def find_by_ids(self, product_ids: List[int]) -> List[Product]:
        return self.db.session.query(Product).filter(Product.id.in_(product_ids)).all()

    def find_all_pageable(self, page, rows_per_page: int = 5):
        return self.db.session.query(Product).order_by(Product.id)\
            .paginate(page=page, per_page=rows_per_page, error_out=False)

    def find_all(self) -> List[Product]:
        return Product.query.all()

    def create(self, item):
        pass

    def update(self, item):
        pass

    def delete(self, item_id):
        pass
