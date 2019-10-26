"""
The file contains the fixtures for tests
"""
import pytest


@pytest.fixture()
def random_dog_url():
    """
The fixture returns the url for the random breed image
    """
    return 'https://dog.ceo/api/breeds/image/random'


@pytest.fixture()
def akita_url():
    """
The fixture returns the url for the akita image
    """
    return 'https://dog.ceo/api/breed/akita/images'


@pytest.fixture(params=["akita", "beagle", "husky"])
def breed_list_url(request):
    """
The parametrized fixture returns the url for the list of different breeds
    """
    return 'https://dog.ceo/api/breed/' + request.param + '/list'


@pytest.fixture()
def list_all_url():
    """
The fixture returns the url for the list of all breeds
    """
    return 'https://dog.ceo/api/breeds/list/all'


@pytest.fixture()
def get_brewery_url():
    """
The fixture returns the url for the list of breweries
    """
    return 'https://api.openbrewerydb.org/breweries'


@pytest.fixture()
def post_url():
    """
The fixture returns the url for the posts
    """
    return 'https://jsonplaceholder.typicode.com/posts'


@pytest.fixture()
def todos_url():
    """
The fixture returns the url for the todos
    """
    return 'https://jsonplaceholder.typicode.com/todos'


@pytest.fixture()
def photo_url():
    """
The fixture returns the url for the photos
    """
    return 'https://jsonplaceholder.typicode.com/photo'


def pytest_addoption(parser):
    """
The function for returning url using addoption
    """
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="The request url for yandex"
    )


@pytest.fixture
def url_param(request):
    """
The fixture returns ya.ru url
    """
    return request.config.getoption("--url")
