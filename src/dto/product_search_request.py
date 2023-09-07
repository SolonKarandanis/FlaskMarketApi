from src.dto.paging import Paging


class ProductSearchRequest:
    def __init__(self, query: str, paging: Paging):
        self.query = query
        self.paging = paging

    def __repr__(self):
        return f"<ProductSearchRequest  query={self.query} , paging={self.paging}>"
