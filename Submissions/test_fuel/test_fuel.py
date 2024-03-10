import pytest
from fuel import convert, gauge


def test_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("7/dog")
    with pytest.raises(ValueError):
        convert("cat/6")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("abcd")
    with pytest.raises(ValueError):
        convert("abcd")
    assert convert("1/2") == 50
    assert convert("1/1") == 100



def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(33) == "33%"
