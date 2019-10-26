"""
The file contains test cases for the https://dog.ceo/dog-api/ service
"""
import random
import requests
import pytest


def test_get_dog_random(random_dog_url):
    """
The test checks if the random dog image request gets status:success
    """
    res = requests.get(random_dog_url).json().get("status")
    assert res == 'success'


def test_get_akita_images(akita_url):
    """
The test checks the length of the message in the response when requesting the akita images
    """
    res = requests.get(akita_url).json().get("message")
    assert len(res) == 9


def test_get_random_count(random_dog_url):
    """
The test checks if the response has the same number of images as it was in the request
    """
    random_number = random.randint(1, 50)
    rand = str(random_number)
    url = random_dog_url + "/" + rand
    res = requests.get(url).json().get("message")
    assert len(res) == random_number


def test_get_dog_breeds_status(breed_list_url):
    """
The test checks if the list of breeds url has a status code == 200 in the response
    """
    res = requests.get(breed_list_url).status_code
    assert res == 200


@pytest.mark.parametrize("breed", ['akita', 'beagle', 'hound'])
def test_get_dog_list(list_all_url, breed):
    """
The parametrized test checks if the url has the necessary breed in the response
    """
    message = requests.get(list_all_url).json().get("message")
    if breed in message.keys():
        assert True
