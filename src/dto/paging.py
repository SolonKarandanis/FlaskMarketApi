class Paging:
    def __init__(self, page: int, limit: int, sort_field: str, sort_direction: str):
        self.page = page
        self.limit = limit
        self.sort_field = sort_field
        self.sort_direction = sort_direction

    def __repr__(self):
        return f"<Paging  page={self.page},limit={self.limit},sort_field={self.sort_field},sort_direction={self.sort_direction}> "