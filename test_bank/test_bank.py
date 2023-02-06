from bank import value
import pytest


def test_hello():
    assert value('hello') == 0

def test_h():
    assert value('h') == 20

def test_empty():
    assert value('') == 100

def test_num():
    with pytest.raises(AttributeError):
        value(5)

def test_cases():
    assert value('Hello') == 0

def test_two_words():
    assert value('whats up?') == 100