from twttr import shorten


def main():
    test_shorten()


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("12345") == "12345"
    assert shorten("") == ""


if __name__ == "__main__":
    main()
