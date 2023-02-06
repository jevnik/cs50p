from seasons import birth_date
import pytest

def test_corr():
    assert (birth_date('1995-12-14').date().day) == 14


def test_wrong_f():
    with pytest.raises(SystemExit):
        birth_date('1995a12-14').date().day

def test_wrong_f2():
    with pytest.raises(SystemExit):
        birth_date('1995.12.14').date().day
