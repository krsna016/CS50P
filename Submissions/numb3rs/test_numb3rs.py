from numb3rs import validate

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("HelloCS50") == False
    assert validate("0.0.0.0") == True
    assert validate("234.255.999.255") == False
    assert validate("234.987.245.123") == False
    assert validate("333.255.245.32") == False
    assert validate("a.b.3.33") == False
    assert validate("234.255.245.666") == False


