import pytest
from fuel import convert, gauge

def test_convert():
    assert round(convert("1/2")) == 50
    assert round(convert("3/4")) == 75
    assert round(convert("2/2")) == 100
    assert round(convert("0/1")) == 0
    assert round(convert("1/3")) == 33
    assert round(convert("2/3")) == 67
    assert round(convert("5/10")) == 50
    assert round(convert("7/8")) == 88
    assert round(convert("1/100")) == 1
    assert round(convert("99/100")) == 99

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(88) == "88%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
