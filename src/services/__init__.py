from src.data_access.repositories import cart_repo, user_repo, product_repo
from src.services.cart_service import CartService
from src.services.email_service import EmailService
from src.services.product_service import ProductService
from src.services.user_service import UserService

email_service = EmailService()
cart_service = CartService(cart_repo)
user_service = UserService(user_repo)
product_service = ProductService(product_repo)
