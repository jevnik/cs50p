from twttr import shorten
import pytest

def test_string():
    assert shorten('abcd') == 'bcd'

def test_String():
    assert shorten('ABcd') == 'Bcd'

def test_punc():
    assert shorten('..abcd') == '..bcd'

def test_num():
    with pytest.raises(TypeError):
        shorten(5)
