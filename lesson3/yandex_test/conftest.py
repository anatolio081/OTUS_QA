import pytest


def pytest_addoption(parser):
    """parser add Option"""
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture
def url_param(request):
    """
    :param request:
    :return:
    """
    return request.config.getoption("--url")