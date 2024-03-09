from bank import value


def test_hello():
    assert value("Hello, Master!!") == 0
    assert value("Hello, You are so beautiful.") == 0


def test_h():
    assert value("Hey, How are you?") == 20
    assert value("Hey, Can you spent time with me !!") == 20


def test_other():
    assert value("I Love you !!") == 100
    assert value("Myself Anurag !!") == 100
