from src import db


class ProductTypeBase(db.DeclarativeBase):
    pass


product_type = db.Table(
    "product_type",
    ProductTypeBase.metadata,
    db.Column("type_id", db.ForeignKey("type.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("product.id"), primary_key=True),
)