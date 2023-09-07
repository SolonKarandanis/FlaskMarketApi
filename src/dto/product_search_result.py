class ProductSearchResult:
    def __init__(self, id: int, sku: str, name: str, supplier: str, description: str, price: float):
        self.id = id
        self.sku = sku
        self.name = name
        self.supplier = supplier
        self.description = description
        self.price = price

    def __repr__(self):
        return f"<ProductSearchResult  id={self.id},sku={self.sku},name={self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'supplier': self.supplier,
            'description': self.description,
            'price': self.price,
        }
