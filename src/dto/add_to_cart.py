class AddToCart:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"<AddToCart  product_id={self.product_id} , quantity={self.quantity}>"