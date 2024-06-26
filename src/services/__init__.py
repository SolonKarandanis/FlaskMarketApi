from flask_mail import Mail

from src.data_access.repositories import cart_repo, user_repo, product_repo, order_repo
from src.services.cart_service import CartService
from src.services.email_service import EmailService
from src.services.order_service import OrderService
from src.services.product_service import ProductService
from src.services.product_search_service import ProductSearchService
from src.services.user_service import UserService


mail = Mail()

email_service = EmailService(mail)
product_service = ProductService(product_repo)
cart_service = CartService(cart_repo, product_repo)
user_service = UserService(user_repo)
order_service = OrderService(order_repo)
product_search_service = ProductSearchService(product_repo)


