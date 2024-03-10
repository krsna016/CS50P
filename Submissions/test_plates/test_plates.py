from plates import is_valid


def test_len():
    assert is_valid("H") == False
    assert is_valid("He") == True
    assert is_valid("Hello") == True
    assert is_valid("HELLO1234") == False


def test_first_two():
    assert is_valid("He") == True
    assert is_valid("H1") == False
    assert is_valid("50") == False


def test_middle_num():
    assert is_valid("He1234") == True
    assert is_valid("HE234O") == False
    assert is_valid("Hee240") == True


def test_first_zero():
    assert is_valid("0hello") == False
    assert is_valid("05") == False
    assert is_valid("hell05") == False
    assert is_valid("hel505") == True


def test_last_number():
    assert is_valid("hel123") == True
    assert is_valid("he1244") == True
    assert is_valid("hello") == True


def test_punctuations():
    assert is_valid("Heloo!") == False
    assert is_valid(",.HHH") == False
    assert is_valid("./:/.") == False
    assert is_valid("CS50") == True




