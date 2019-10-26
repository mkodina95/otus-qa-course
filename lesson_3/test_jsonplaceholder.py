"""
The file contains test cases for the https://jsonplaceholder.typicode.com/ service
"""
import random
import pytest
import requests


def test_posts_by_user_id(post_url):
    """
The test checks if every userId has 10 posts
    """
    for user_id in range(1, 10):
        user_id = str(int(user_id))
        url = post_url + '?userId=' + user_id
        res = requests.get(url).json()
        assert len(res) == 10


def test_posts_by_id(post_url):
    """
The test checks if the post has the correct id
    """
    random_number = random.randint(1, 100)
    rand = str(random_number)
    url = post_url + '/' + rand
    res = requests.get(url).json().get("id")
    assert res == random_number


@pytest.mark.parametrize('email',
                         ['Eliseo@gardner.biz',
                          'Jayne_Kuhic@sydney.com',
                          'Jeffery@juwan.us'])
def test_email_in_comments(post_url, email):
    """
The test check if the post has the comments with the expected email
    """
    url = post_url + '/2/comments'
    res = requests.get(url).json()
    for obj in res:
        if obj['email'] == email:
            assert True


def test_todos_complete(todos_url):
    """
The test checks if the status of every todos is boolean
    """
    res = requests.get(todos_url).json()
    for obj in res:
        if obj['completed'] == bool:
            assert True


def test_photo_url(photo_url):
    """
The test checks if all urls with photo begin with the substring https://via.placeholder.com/600/
    """
    res = requests.get(photo_url).json()
    for obj in res:
        if obj['url'][:-6] == 'https://via.placeholder.com/600/':
            assert True
