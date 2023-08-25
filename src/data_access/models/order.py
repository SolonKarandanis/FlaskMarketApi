from datetime import datetime
from typing import List

from src import db
from src.data_access.models import cart_item
from src.data_access.models.order_item import OrderItem
from src.data_access.models.user import User


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, db.Sequence("orders_sq", start=1), primary_key=True)
    date_created = db.Column(db.Date())
    status = db.Column(db.String(length=40))
    total_price = db.Column(db.Float)
    comments = db.Column(db.String(length=2048))
    order_items = db.relationship('OrderItem', backref="order")
    users_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return f"<Order {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'total_price': self.total_price,
            'date_created': self.date_created,
            'status': self.status,
            'comments': self.comments,
            'users_id': self.users_id,
            'order_items': [order_item.to_dict() for order_item in self.order_items]
        }

    def add_order_items(self, cart_items: List[CartItem]) -> None:
        for cart_item in cart_items:
            order_item = OrderItem(product_id=cart_item.products_id,
                                   product_name=cart_item.product.name,
                                   sku=cart_item.product.sku,
                                   manufacturer=cart_item.product.supplier,
                                   start_date=datetime.now(),
                                   status=self.status,
                                   price=cart_item.unit_price,
                                   quantity=cart_item.quantity,
                                   total_price=cart_item.total_price)
            self.order_items.append(order_item)