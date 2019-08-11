import pytest


@pytest.fixture(scope="function", params=["1", "2", "3", "4", "5"])
def p_id(request):
    """Параметр идентификатора"""
    return request.param

