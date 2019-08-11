import pytest


@pytest.fixture(scope="function", params=["1", "2", "3"])
def p_number(request):
    return request.param