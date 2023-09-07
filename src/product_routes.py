import logging

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from src.constants.http_status_codes import HTTP_200_OK
from src.decorators.convert_input_to import convert_input_to
from src.dto.product_search_request import ProductSearchRequest
from src.services import product_service, product_search_service

products = Blueprint("products", __name__, url_prefix="/market/v1/products")

logger = logging.getLogger(__name__)

@products.get("/")
@jwt_required()
def fetch_products():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    result = product_service.find_all_pageable(page, limit)

    meta = {
        "page": result.page,
        'pages': result.pages,
        'total_count': result.total,
        'prev_page': result.prev_num,
        'next_page': result.next_num,
        'has_next': result.has_next,
        'has_prev': result.has_prev,
    }

    return jsonify({'data': [p.to_dict() for p in result.items], "meta": meta}), HTTP_200_OK


@products.post("/search")
@jwt_required()
@convert_input_to(ProductSearchRequest)
def search_products(product_search_request: ProductSearchRequest):
    logger.info(f'search request {product_search_request}')
    result = product_search_service.query_product_index(product_search_request)
    logger.info(f'search result {result}')
    return result.to_dict(), HTTP_200_OK


@products.get("/<int:product_id>")
@jwt_required()
def get_product(product_id):
    product = product_service.find_by_id(product_id)
    result = product.to_dict()

    return result, HTTP_200_OK


@products.get("/index")
@jwt_required()
def index():
    product_search_service.add_to_product_index()
    return {}, HTTP_200_OK
