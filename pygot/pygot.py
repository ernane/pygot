from simple_rest_client.exceptions import NotFoundError

from pygot.api import create_api
from pygot.api.resources import fetch_resources
from pygot.models.book import BookSchema


class Pygot:
    def __init__(self) -> None:
        self._api = create_api()

    def houses(self):
        return fetch_resources(endpoint="houses")

    def books(self):
        return fetch_resources(
            api=self._api, endpoint="books", schema=BookSchema(many=True)
        )

    def find_book(self, params):
        return BookSchema(many=True).load(self._api.books.list(params=params).body)

    def book(self, id):
        try:
            return BookSchema().load(self._api.books.show(id).body)
        except NotFoundError:
            raise Exception("Book Not Found")
