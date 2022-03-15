import pytest
from click.testing import CliRunner

from pygot import Pygot
from pygot.api import create_api


@pytest.fixture(scope="module")
def api():
    return create_api()


@pytest.fixture(scope="module")
def app():
    return Pygot()


@pytest.fixture(scope="module")
def cli_runner():
    return CliRunner()
