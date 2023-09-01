import logging

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.constants.http_status_codes import HTTP_200_OK
from src.services import cart_service, order_service

orders = Blueprint("orders", __name__, url_prefix="/market/v1/orders")
logger = logging.getLogger(__name__)


@orders.post("/")
@jwt_required()
def place_order():
    order_comments = request.args.get('comments', '', type=str)
    user_id = get_jwt_identity()
    cart = cart_service.find_with_items_and_products_by_user_id(user_id)
    order = order_service.add_order_items(user_id,cart,order_comments)
    cart.clear_cart()
    cart_service.update_cart(cart)
    return order.to_dict(), HTTP_200_OK


@orders.get("/<int:order_id>")
@jwt_required()
def get_order(order_id):
    user_id = get_jwt_identity()
    order = order_service.find_by_user_and_id(user_id, order_id)
    return order.to_dict(), HTTP_200_OK
