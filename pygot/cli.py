import json

import click

from pygot.models.book import BookSchema
from pygot.pygot import Pygot

pygot = Pygot()

book_schema = BookSchema()


@click.group()
def cli():
    pass


@cli.command(help="List all houses")
def houses():
    for house in pygot.houses():
        click.echo(house.name)


@cli.command(help="List all books")
def books():
    for book in pygot.books():
        click.echo(book.name)


@cli.command(help="Get specific book")
@click.option(
    "--id",
    required=True,
    help="Book Id.",
)
def book(id):
    click.echo(json.dumps(book_schema.dump(pygot.book(id)), indent=2))


@cli.command(
    name="filtering_books",
    help="Filtering books with name, fromReleaseDate or toReleaseDate",
)
@click.option(
    "--name",
    help="Books with the given name.",
)
@click.option(
    "--from_release_date",
    help="Books that were released after, or on, the given date.",
)
@click.option(
    "--to_release_date",
    help="Books that were released before, or on, the given date.",
)
def filtering_books(name=None, from_release_date=None, to_release_date=None):
    params = {
        "name": name,
        "fromReleaseDate": from_release_date,
        "toReleaseDate": to_release_date,
    }
    books = pygot.find_book(params)

    for book in books:
        click.echo(json.dumps(book_schema.dump(book), indent=2))


@cli.command(help="List all characters")
def characters():
    for character in pygot.characters():
        click.echo(character.name)


if __name__ == "__main__":
    cli()

# https://github.com/daneoshiga/sentry-patrol/blob/master/tests/test_patrol.py
# https://dev.to/bowmanjd/build-a-command-line-interface-with-python-poetry-and-click-1f5k
