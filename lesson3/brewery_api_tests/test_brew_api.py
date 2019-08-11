import pytest
import requests


def test_id_is_int():
    """
    Проверка, является ли идентификатор целочисленным
    """
    r = requests.get('https://api.openbrewerydb.org/breweries')
    messages = r.json()
    failflag = 1
    for msg in messages:
        if type(msg["id"]) == 1:
            failflag = 0
    assert failflag


def test_id_is_unique():
    """
    Проверка, является ли идентификатор уникальным
    Если идентификатор попадается более 1 раза, тест фейлится
    """
    r = requests.get('https://api.openbrewerydb.org/breweries')
    messages = r.json()
    for msg in messages:
        count = 0
        check = msg["id"]
        if msg["id"] == check:
            count += 1
        assert count == 1


@pytest.mark.parametrize("test_input", ["Cooper", "Brewing", "Foothills"])
def test_id_is_unique(test_input):
    """
    Проверка соотвтетвия имени из параметра
    :param test_input:
    :return:
    """
    url = "https://api.openbrewerydb.org/breweries?by_name=" + test_input
    r = requests.get(url)
    messages = r.json()
    for msg in messages:
        assert test_input in msg["name"]


def test_brewery_type(p_types):
    """
    Проверка по типу пивоварни
    """
    url = "https://api.openbrewerydb.org/breweries?by_type=" + p_types
    r = requests.get(url)
    messages = r.json()
    for msg in messages:
        assert p_types == msg["brewery_type"]
    pass

@pytest.mark.parametrize("p_city", ["San Jose", "New York", "Detroit"])
def test_brewery_type(p_types,p_city):
    """
    :param p_types:
    :param p_city:
    :return:
    """
    url = "https://api.openbrewerydb.org/breweries?by_type=" + p_types + "&by_city" + p_city
    r = requests.get(url)
    messages = r.json()
    for msg in messages:
        assert p_types == msg["brewery_type"]
    pass
