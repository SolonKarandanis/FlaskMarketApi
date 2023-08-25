from src import db
from src.data_access.models import product, order


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column(db.Integer, db.Sequence("order_items_sq", start=1), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    orders_id = db.Column(db.Integer, db.ForeignKey(Order.id))
    product_name = db.Column(db.String(length=255), nullable=False)
    sku = db.Column(db.String(length=255), nullable=False)
    manufacturer = db.Column(db.String(length=255), nullable=False)
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    status = db.Column(db.String(length=40))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)

    def __repr__(self):
        return f"<OrderItem {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'orders_id': self.orders_id,
            'product_name': self.product_name,
            'sku': self.sku,
            'manufacturer': self.manufacturer,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'status': self.status,
            'price': self.price,
            'quantity': self.quantity,
            'total_price': self.total_price,
        }