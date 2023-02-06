from fuel import convert,gauge
from pytest import raises

def test_convert_q():
    assert convert('1/4') == 25

def test_convert_zero():
    assert convert('0/4') == 0

def test_convert_one():
    assert convert('4/4') == 100

def test_convert_str():
    with raises(ValueError):
        convert('a')

def test_convert_str_div():
    with raises(ValueError):
        convert('1/a')

def test_convert_str_div_and_up():
    with raises(ValueError):
        convert('b/a')

def test_convert_str_div():
    with raises(ValueError):
        convert('.')

def test_convert_str_sign():
    with raises(ValueError):
        convert('1(3')

def test_convert_zero():
    with raises(ZeroDivisionError):
        convert('2/0')

def test_convert_list():
    with raises(AttributeError):
        convert([1])

def test_convert_empty():
    with raises(ValueError):
        convert('')


def test_gauge_one():
    assert gauge(1) == 'E'

def test_gauge_less_one():
    assert gauge(0.5) == 'E'

def test_gauge_f():
    assert gauge(99) == 'F'

def test_gauge():
    assert gauge(50) == '50%'
