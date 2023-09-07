import logging

from flask import current_app

from src.dto.product_search_response import ProductSearchResponse
from src.dto.product_search_result import ProductSearchResult

logger = logging.getLogger(__name__)


class FtsRepository:

    def add_to_index(self, index, model):
        logger.info(f'index: {index}')
        logger.info(f'model: {model}')
        if not current_app.elasticsearch:
            return
        payload = {}
        for field in model.__searchable__:
            logger.info(f'field: {field}')
            payload[field] = getattr(model, field)
        current_app.elasticsearch.index(index=index, id=model.id, body=payload)

    def remove_from_index(self, index, model):
        if not current_app.elasticsearch:
            return
        current_app.elasticsearch.delete(index=index, id=model.id)

    def query_index(self, index, query, page, per_page):
        if not current_app.elasticsearch:
            return [], 0
        search = current_app.elasticsearch.search(
            index=index,
            body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
                  'from': (page - 1) * per_page, 'size': per_page})
        total = search['hits']['total']['value']
        content = [ProductSearchResult(**hit['_source']) for hit in search['hits']['hits']]
        response = ProductSearchResponse(content, total)
        return response
