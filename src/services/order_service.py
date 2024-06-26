from src.data_access.models.models import Order, Cart
from src.data_access.repositories import OrderRepository


class OrderService:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def find_by_user_and_id(self, user_id: int, order_id: int) -> Order:
        return self.repo.find_by_user_and_id(user_id, order_id)

    def create(self, user_id: int, total_price: float, order_comments: str) -> Order:
        return self.repo.create(user_id, total_price, order_comments)

    def update_order(self, order: Order) -> Order:
        return self.repo.update(order)

    def add_order_items(self, user_id: int, cart: Cart, order_comments: str) -> Order:
        order = self.create(user_id, cart.total_price, order_comments)
        cart_items = cart.cart_items
        order.add_order_items(cart_items)
        order = self.update_order(order)
        return order
