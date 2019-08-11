import pytest
import requests


def test_get_200(url_param):
    """
    получить ya.ru через getoption
    :param url_param:
    :return:
    """
    r = requests.get(url_param)
    assert r.status_code == 200
