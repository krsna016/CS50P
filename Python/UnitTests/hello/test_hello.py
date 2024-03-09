from hello import hello


def test_default():
    assert hello() == "Hello, Krsna"


def test_argument():
    assert hello("Anurag") == "Hello, Anurag"
