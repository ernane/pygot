import pytest

from pygot.models.book import Book
from pygot.models.character import Character
from pygot.models.house import House


def test_book(app):
    book = app.book(1)
    assert isinstance(book, Book)
    assert repr(book) == "<Book(name='A Game of Thrones')>"


def test_book_exception(app):
    with pytest.raises(Exception):
        assert app.book(-1)


def test_books(app):
    books = app.find_book({})
    assert isinstance(books, list)


def test_house(app):
    house = app.house(1)
    assert isinstance(house, House)
    assert repr(house) == "<House(name='House Algood')>"


def test_house_exception(app):
    with pytest.raises(Exception):
        assert app.house(-1)


def test_houses(app):
    houses = app.find_house({})
    assert isinstance(houses, list)


def test_character(app):
    character = app.character(2)
    assert isinstance(character, Character)
    assert repr(character) == "<Character(name='Walder')>"


def test_character_exception(app):
    with pytest.raises(Exception):
        assert app.character(-1)


def test_characters(app):
    characters = app.find_character({})
    assert isinstance(characters, list)
