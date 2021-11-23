import pytest
from simple_rest_client.resource import Resource

from pygot.models.book import BookSchema


def test_get_api_instance(api):
    assert api.api_root_url == "https://www.anapioficeandfire.com/api"
    assert api.headers["Content-Type"] == "application/json"
    assert api.json_encode_body


def test_get_resource_instance(api):
    assert isinstance(api.books, Resource)
    assert isinstance(api.characters, Resource)
    assert isinstance(api.houses, Resource)


def test_get_resource_list(api):
    resource_list = api.get_resource_list()
    assert "books" in resource_list
    assert "characters" in resource_list
    assert "houses" in resource_list


@pytest.mark.parametrize(
    "url,method,status,action,args,kwargs",
    [
        ("/books", "GET", 200, "list", None, {}),
        ("/books/1", "GET", 200, "show", 1, {}),
    ],
)
def test_request_api_books_actions(
    httpserver, url, method, status, action, args, kwargs, api
):
    httpserver.expect_request(url, method=method).respond_with_json(
        {"success": True}, status=status
    )

    response = getattr(api.books, action)(args, **kwargs)
    assert response.status_code == status
    assert response.method == method
    assert url in response.url


@pytest.mark.parametrize(
    "url,method,status,action,args,kwargs",
    [
        ("/books/1", "GET", 200, "show", 1, {}),
    ],
)
def test_request_api_book(httpserver, url, method, status, action, args, kwargs, api):
    httpserver.expect_request(url, method=method).respond_with_json(
        {"success": True}, status=status
    )

    response = getattr(api.books, action)(args, **kwargs)

    assert BookSchema().validate(response.body) == {}


@pytest.mark.parametrize(
    "url,method,status,action,args,kwargs",
    [
        ("/characters", "GET", 200, "list", None, {}),
        ("/characters/1", "GET", 200, "show", 1, {}),
    ],
)
def test_request_api_characters_actions(
    httpserver, url, method, status, action, args, kwargs, api
):
    httpserver.expect_request(url, method=method).respond_with_json(
        {"success": True}, status=status
    )

    response = getattr(api.characters, action)(args, **kwargs)
    assert response.status_code == status
    assert response.method == method
    assert url in response.url


@pytest.mark.parametrize(
    "url,method,status,action,args,kwargs",
    [
        ("/houses", "GET", 200, "list", None, {}),
        ("/houses/1", "GET", 200, "show", 1, {}),
    ],
)
def test_request_api_houses_actions(
    httpserver, url, method, status, action, args, kwargs, api
):
    httpserver.expect_request(url, method=method).respond_with_json(
        {"success": True}, status=status
    )

    response = getattr(api.houses, action)(args, **kwargs)
    assert response.status_code == status
    assert response.method == method
    assert url in response.url
