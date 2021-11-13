import pytest

from pygot import Pygot
from pygot.api import create_api


@pytest.fixture(scope="module")
def api():
    return create_api()


@pytest.fixture(scope="module")
def app():
    return Pygot()
