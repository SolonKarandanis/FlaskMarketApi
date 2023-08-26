from src.data_access.models.models import Cart
from src.data_access.repositories import CartRepository


class CartService:
    def __init__(self, repo: CartRepository):
        self.repo = repo

    def find_with_items_by_user_id(self, user_id: int) -> Cart:
        return self.repo.find_with_items_by_user_id(user_id)

    def find_with_items_and_products_by_user_id(self, user_id: int) -> Cart:
        return self.repo.find_with_items_and_products_by_user_id(user_id)

    def create(self, user_id: int) -> Cart:
        return self.repo.create(user_id)

    def fetch_or_create_cart(self, user_id: int) -> Cart:
        cart = self.find_with_items_by_user_id(user_id)
        if cart is None:
            cart = self.create(user_id)
        return cart

    def update_cart(self, cart: Cart) -> Cart:
        return self.repo.update(cart)

    def delete_cart_item(self, user_id: int, item_id: int) -> None:
        cart = self.find_with_items_by_user_id(user_id)
        cart_item = next(filter(lambda ci: ci.id == item_id, cart.cart_items), None)
        if cart_item is not None:
            cart.remove_from_cart(cart_item)
            self.update_cart(cart)

    def update_item_quantity(self, user_id: int, item_id: int, quantity: int) -> Cart:
        cart = self.find_with_items_by_user_id(user_id)
        cart.update_item_quantity(item_id, quantity)
        self.update_cart(cart)
        return cart

    def add_to_cart(self, user_id: int) -> Cart:
        cart = self.fetch_or_create_cart(user_id)

        return cart
