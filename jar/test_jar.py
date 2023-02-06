from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

def test_str():
    jar_str = Jar()
    assert print(jar_str) == None

def test_dep():
    jar_dep = Jar()
    jar_dep.deposit(2)
    assert jar_dep.__str__() == '🍪🍪'

def test_with():
    jar_with = Jar()
    jar_with.deposit(5)
    jar_with.withdraw(2)
    assert jar_with.__str__() == '🍪🍪🍪'

def test_overload():
    jar_over = Jar()
    jar_over.deposit(5)
    with pytest.raises(ValueError):
        jar_over.deposit(12)

def test_overwith():
    jar_overwith = Jar()
    jar_overwith.deposit(4)
    with pytest.raises(ValueError):
        jar_overwith.withdraw(12)

def test_neg_cap():
    with pytest.raises(ValueError):
        jar = Jar(-2)
