from src import db
from src.data_access.models import product, cart


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, db.Sequence("cart_items_sq", start=1), primary_key=True)
    quantity = db.Column(db.Integer)
    modification_alert = db.Column(db.Boolean())
    unit_price = db.Column(db.Float)
    total_price = db.Column(db.Float)
    carts_id = db.Column(db.Integer, db.ForeignKey(Cart.id))
    products_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    product = db.relationship(Product, backref="cart_items")

    def __repr__(self):
        return f"<CartItem {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'total_price': self.total_price,
            'carts_id': self.carts_id,
            'products_id': self.products_id,
        }