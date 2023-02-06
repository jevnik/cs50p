from plates import is_valid

def test_len_less_two():
    assert is_valid('c') == False

def test_len_more_seven():
    assert is_valid('cs500000') == False

def test_num_mid():
    assert is_valid('cs55aa') == False

def test_ok():
    assert is_valid('cs50') == True

def test_num_beg():
    assert is_valid('50cs22') == False

def test_first_num_zero():
    assert is_valid('cs05') == False

def test_num_first():
    assert is_valid('50cs') == False

def test_no_alpha():
    assert is_valid('5555') == False

def test_punc():
    assert is_valid('ab2..4') == False


