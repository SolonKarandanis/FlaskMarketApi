from typing import List

from src.dto.product_search_result import ProductSearchResult


class ProductSearchResponse:
    def __init__(self, content: List[ProductSearchResult], total: int):
        self.content = content
        self.total = total

    def __repr__(self):
        return f"<ProductSearchResult  total={self.total},content={self.content}>"
