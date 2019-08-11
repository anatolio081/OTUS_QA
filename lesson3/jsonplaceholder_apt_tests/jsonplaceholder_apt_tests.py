import pytest
import requests
import validators

def test_id_is_int():
    """
    Проверка наличия имен в поле username
    """
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    messages = r.json()
    for msg in messages:
        assert not (msg["username"] == "")


def test_id_is_int():
    """
    Проверка итеративности идентификаторов
    """
    r = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
    messages = r.json()
    i = 0
    for msg in messages:
        i += 1
        assert msg["id"] == i


def test_anti_dubl(p_id):
    """
        Проверка отсутствия дубликатов поля body
    """
    r = requests.get('https://jsonplaceholder.typicode.com/comments?postId=' + p_id)
    messages = r.json()
    i = 0
    for msg in messages:
        count = 0
        check = msg["body"]
        if msg["body"] == check:
            count += 1
        assert count == 1


def test_user_id_posts(p_id):
    """
        Проверка соответствия идентификатора user_id в выборке постов
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts?userId=' + p_id)
    messages = r.json()
    for msg in messages:
        assert msg["userId"] == int(p_id)


@pytest.mark.parametrize("param_id", ["1", "2", "3"])
def test_user_id_posts(param_id):
    """
        Валидация url для изображений
    """
    r = requests.get('https://jsonplaceholder.typicode.com/photos?albumId=' + param_id)
    messages = r.json()
    for msg in messages:
        assert validators.url(msg["url"])
