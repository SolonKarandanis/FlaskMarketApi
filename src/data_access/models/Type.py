from src import db
from src.data_access.models.ProductTypeBase import ProductTypeBase


class Type(ProductTypeBase):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(length=30), nullable=False)

    def __repr__(self):
        return f"<Type {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type_name,
        }