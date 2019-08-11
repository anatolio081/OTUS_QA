import pytest


@pytest.fixture(scope="function", params=["1", "2", "3"])
def p_number(request):
    """параметр, для запроса колличества рандомных сообщений"""
    return request.param