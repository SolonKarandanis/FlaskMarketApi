from flask import Blueprint, jsonify

products = Blueprint("products", __name__, url_prefix="/market/v1/products")