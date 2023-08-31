from typing import List

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.constants.http_status_codes import HTTP_204_NO_CONTENT, HTTP_200_OK
from src.decorators.convert_input_to import convert_input_to
from src.dto.add_to_cart import AddToCart
from src.services import cart_service
import logging

carts = Blueprint("carts", __name__, url_prefix="/market/v1/carts")
logger = logging.getLogger(__name__)


@carts.get("/")
@jwt_required()
def get_user_cart():
    user_id = get_jwt_identity()
    cart = cart_service.fetch_or_create_cart(user_id)
    return cart.to_dict(), HTTP_200_OK


@carts.post("/")
@jwt_required()
@convert_input_to(AddToCart)
def add_to_cart(add_to_cart_request: List[AddToCart]):
    user_id = get_jwt_identity()
    logger.info(f'data: {add_to_cart_request}')
    return {},HTTP_200_OK


@carts.delete("/<int:item_id>/delete")
@jwt_required()
def delete_cart_item(item_id):
    user_id = get_jwt_identity()
    cart_service.delete_cart_item(user_id, item_id)
    return jsonify({}), HTTP_204_NO_CONTENT


@carts.post("/<int:item_id>/update")
@jwt_required()
def update_cart_item_quantity(item_id):
    user_id = get_jwt_identity()
    quantity = request.args.get('quantity', type=int)
    cart = cart_service.update_item_quantity(user_id, item_id, quantity)
    return cart.to_dict(), HTTP_200_OK
