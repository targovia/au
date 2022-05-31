
import pytest

@pytest.fixture
def setUp():
    print("SET3 FIXTURE MODULE")
    print("SET3 FIXTURE MODULE")
    print("SET3 FIXTURE MODULE")
    yield
    print("GASI TOKA")


def test_test101(setUp):
    print("THIS IS TEST101")

def test_test102(setUp):
    print("THIS IS TEST102")

def test_test103():
    print("THIS IS TEST103")

def test_test104():
    print("THIS IS TEST104")

def test_test105():
    print("THIS IS TEST105")