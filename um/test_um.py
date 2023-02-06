from um import count

def test_num():
    assert count('um 555 um') == 2

def test_caps():
    assert count('UM AAA UM BBB') == 2

def test_repeat():
    assert count('um um') == 2

def test_symbols():
    assert count('!!! um !!') == 1

def test_mixed_caps():
    assert count('Um Um Um') == 3

def test_word_start_with():
    assert count('umbrella') == 0

def test_word_ends_with():
    assert count('sunum') == 0

def test_ends():
    assert count('aaa um') == 1

def test_pun():
    assert count('um, um') == 2

def test_pun_b():
    assert count(':um um') == 2

def test_pun_both():
    assert count(' :um, um um') == 3