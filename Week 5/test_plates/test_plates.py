from plates import is_valid


def main():
    test_is_valid()


def test_is_valid():

    test_cases = {

        "ABC123": True,
        "A1": False,
        "A01": False,
        "A123": False,
        "123ABC": False,
        "AB": True,
        "A": False,
        "ABCD1234": False,
        "A B C 123": False,
        "ABCD": True,
        "AB1234": True,
        "A1B2C3": False,
        "AB01": False,
        "ABCD0": False,
        "AB123": True,
        "XYZ999": True,
        "ABCDE": True,
        "AB1C2D": False,
        "AB01CD": False,
        "AB12345": False,
        "A B C": False,
        "AB1!@": False,
        "12ABCD": False,
        "A0B": False,
    }

    for plate, expected in test_cases.items():
        assert is_valid(plate) == expected


if __name__ == "__main__":
    main()
