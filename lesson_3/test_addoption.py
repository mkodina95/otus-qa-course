"""
The file contains the test for ya.ru
"""
import requests


def test_yandex_status_code(url_param):
    """
The test checks if url returns status_code == 200
    """
    res = requests.get(url_param).status_code
    assert res == 200
