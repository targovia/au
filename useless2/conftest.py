import pytest


@pytest.fixture(autouse=True)
def test_beforeandafter():
    print("Fixture1")
    print("Fixture2")
    yield
    print("Gasi toka otzzad")