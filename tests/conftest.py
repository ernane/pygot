import pytest

from pygot.api import create_api


@pytest.fixture(scope="module")
def api():
    return create_api()
