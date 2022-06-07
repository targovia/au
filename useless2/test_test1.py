import pytest


def test_te1():
    print("Content of test1")

def test_te2():
    print("Content of test2")

def test_te3():
    print("Content of test3")

def test_te4():
    print("Content of test4")

@pytest.mark.parametrize("a, b, c", [(2, 2, 4), (5, 9, 14), (5, 5, 10)])
def test_te5(a, b, c):
    assert a + b == c