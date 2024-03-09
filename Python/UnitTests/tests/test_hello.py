import sys
sys.path.append("/Users/anuragpareek/Desktop/CS50P/Python/UnitTests/hello")
from hello import hello

def test_default():
    assert hello() == "Hello, Krsna"


def test_argument():
    assert hello("Anurag") == "Hello, Anurag"
