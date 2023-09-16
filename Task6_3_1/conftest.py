import pytest


def pytest_addoption(parser):
    parser.addoption("--rounding_index", default=3)
 #   parser.addoption("--rounding_index", action="store", default=1)


@pytest.fixture
def rounding_index(request):
    return request.config.getoption("--rounding_index")
