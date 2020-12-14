import pytest


@pytest.fixture(scope="module")
def fixtureconftest():
    print("这是conftest里面的fixture")
    yield
    print("这是conftest里面的fixture的结束")
