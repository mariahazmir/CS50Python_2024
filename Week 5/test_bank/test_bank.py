from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value(" hello ") == 0

def test_h_starts():
    assert value("hi") == 20
    assert value("howdy") == 20
    assert value("hey") == 20
    assert value("Hike") == 20

def test_other():
    assert value("goodbye") == 100
    assert value("world") == 100
    assert value("CS50") == 100
    assert value("what's up!") == 100

