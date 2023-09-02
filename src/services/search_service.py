from flask import current_app

from src.data_access.fts import FtsRepository


class SearchService:
    def __init__(self, repo: FtsRepository):
        self.repo = repo

    def add_to_index(self, index, model):
        pass

    def remove_from_index(self, index, model):
        pass

    def query_index(self, index, query, page, per_page):
        pass
