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
