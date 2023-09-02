from src.data_access.models.models import Product


class ProductSearchService:

    def add_to_product_index(self, objects_to_be_indexed) -> None:
        Product.reindex(objects_to_be_indexed)

    def remove_from_product_index(self, index, model):
        pass

    def query_product_index(self, query, page, per_page):
        return Product.search(query, page, per_page)
