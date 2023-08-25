from src import db
from src.data_access.models.ProductTypeBase import ProductTypeBase, product_type
from typing import Set

from src.data_access.models.Type import Type


class Product(ProductTypeBase):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(length=255), nullable=False)
    name = db.Column(db.String(length=255), nullable=False)
    supplier = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float)
    types: db.Mapped[Set[Type]] = db.relationship('Type', secondary=product_type, )

    @property
    def inline_types(self):
        types_list = list(self.types)
        if len(types_list) == 1:
            return types_list[0].type_name
        else:
            type_names = [tl.type_name for tl in types_list]
            comma_separated_strings = ','.join(type_names)
            return comma_separated_strings

    def __repr__(self):
        return f"<Product {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'supplier': self.supplier,
            'description': self.description,
            'price': self.price,
        }