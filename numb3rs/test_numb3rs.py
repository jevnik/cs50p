from numb3rs import validate

def test_validate():
    assert validate('255.255.255.255') == True
    assert validate('2.') == False
    assert validate('211.') == False
    assert validate('211.') == False
    assert validate('8.8.8.8') == True
    assert validate('2.2.2.2') == True
    assert validate('10.10.10.10') == True
    assert validate('a.2.2.2') == False
    assert validate('2.a.2.2') == False
    assert validate('2.2.a.2') == False
    assert validate('2.2.2.a') == False
    assert validate('256.256.256.256') == False
    assert validate('267.257.257.257') == False
    assert validate('300.300.300.300') == False
    assert validate('2.2.2.2.') == False
    assert validate('.2.2.2.2.') == False

    assert validate('1.2.3.1000') == False
    assert validate('cat') == False