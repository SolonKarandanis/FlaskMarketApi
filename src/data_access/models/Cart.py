from src import db
from src.data_access.models.CartItem import CartItem
from src.data_access.models.user import User


class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, db.Sequence("carts_sq", start=1), primary_key=True)
    total_price = db.Column(db.Float)
    modification_alert = db.Column(db.Boolean())
    date_created = db.Column(db.DateTime(timezone=True))
    date_modified = db.Column(db.DateTime(timezone=True))
    cart_items = db.relationship('CartItem', backref="cart", cascade="all, delete-orphan")
    users_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def add_item_to_cart(self, products_id: int, quantity: int, price: float) -> None:
        existing_cart_item = next(filter(lambda ci: ci.products_id == products_id, self.cart_items), None)
        if existing_cart_item is None:
            cart_item = CartItem(quantity=quantity,
                                 modification_alert=False,
                                 unit_price=price,
                                 total_price=quantity * price,
                                 products_id=products_id)
            self.cart_items.append(cart_item)
        else:
            new_quantity = existing_cart_item.quantity + quantity
            existing_cart_item.quantity = new_quantity
            existing_cart_item.total_price = new_quantity * price

        self.update_cart_total_price()

    def update_item_quantity(self, cart_item_id: int, quantity: int) -> None:
        existing_cart_item = next(filter(lambda ci: ci.id == cart_item_id, self.cart_items), None)
        existing_cart_item.quantity = quantity
        existing_cart_item.total_price = quantity * existing_cart_item.unit_price
        self.update_cart_total_price()

    def remove_from_cart(self, cart_item) -> None:
        self.cart_items.remove(cart_item)
        self.update_cart_total_price()

    def clear_cart(self) -> None:
        self.cart_items.clear()
        self.update_cart_total_price()

    def update_cart_total_price(self) -> None:
        self.total_price = sum(ci.total_price for ci in self.cart_items)

    def __repr__(self):
        return f"<Cart {self.id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'total_price': self.total_price,
            'date_created': self.date_created,
            'date_modified': self.date_modified,
            'cart_items': [cart_item.to_dict() for cart_item in self.cart_items],
            'users_id': self.users_id,
        }