"""
The file contains test cases for the https://www.openbrewerydb.org/ service
"""
import random
import pytest
import requests


def test_get_random_brewery(get_brewery_url):
    """
The test checks if the id's in the response have the same values as the random number
    """
    random_number = random.randint(1, 8029)
    rand = str(random_number)
    url = get_brewery_url + '/' + rand
    res = requests.get(url).json().get("id")
    assert res == random_number


@pytest.mark.parametrize("state", ['Alaska', 'Alabama', 'Ohio'])
def test_get_brewery_by_state(get_brewery_url, state):
    """
The parametrized test checks if the list of breweries sorted by the state
has the necessary value of state in the response
    """
    url = get_brewery_url + '?by_state=' + state
    res = requests.get(url).json()
    for obj in res:
        if obj['state'] != state:
            assert False
    assert True


def test_get_brewery_sort_by_id(get_brewery_url):
    """
The test checks if the list sorted by id's is sorted in the correct sequence
    """
    url = get_brewery_url + '?sort=id'
    res = requests.get(url).json()
    temp_value = res[0]['id']
    index = 1
    while index < len(res):
        if res[index]['id'] - temp_value == 1:
            temp_value = res[index]['id']
            index += 1
        else:
            assert False


def test_get_brewery_per_page(get_brewery_url):
    """
The test checks if the response has the correct number of breweries
    """
    random_number = random.randint(1, 50)
    rand = str(random_number)
    url = get_brewery_url + '?per_page=' + rand
    res = requests.get(url).json()
    assert len(res) == random_number


@pytest.mark.parametrize("tag", ['dog-friendly', 'food-service', 'food-truck', 'tours'])
def test_get_brewery_by_tag(get_brewery_url, tag):
    """
The parametrized test checks if the request with the tag has the empty response
    """
    url = get_brewery_url + '?by_tag=' + tag
    res = requests.get(url).json()
    assert res == []
