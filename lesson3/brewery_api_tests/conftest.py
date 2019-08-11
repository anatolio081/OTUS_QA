import pytest


@pytest.fixture(scope="function", params=["micro", "regional", "brewpub", "bar", "contract", "proprietor"])
def p_types(request):
    """Параметр типов пабов"""
    return request.param

