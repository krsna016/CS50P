from twttr import shorten


def test_strings():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Anurag") == "nrg"
    assert shorten("Radha") == "Rdh"
    assert shorten("Krsna") == "Krsn"


def test_numbers():
    assert shorten("10") == "10"
    assert shorten("101") == "101"
    assert shorten("0") == "0"

def test_punctuations():
    assert shorten("Anurag,s") == "nrg,s"
