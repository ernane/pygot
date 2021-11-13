from pygot.models.book import Book


def test_book(app):
    book = app.book(1)
    assert isinstance(book, Book)
    assert repr(book) == "<Book(name='A Game of Thrones')>"
