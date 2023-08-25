from src.data_access import cart_repo, user_repo
from src.services.cart_service import CartService
from src.services.email_service import EmailService
from src.services.user_service import UserService

email_service = EmailService()
cart_service = CartService(cart_repo)
user_service = UserService(user_repo)