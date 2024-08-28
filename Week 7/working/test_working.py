from working import convert

def test_convert():

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:00 AM") == "22:30 to 08:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1:15 AM to 2:00 PM") == "01:15 to 14:00"

    invalid_cases = [
        "13 AM to 14 PM",
        "9:60 AM to 10:00 AM",
        "9AM to 5PM",
        "9:00 to 5:00",
        "9 AM - 5 PM",
    ]

    for case in invalid_cases:
        try:
            convert(case)
        except ValueError:
            pass
        else:
            raise AssertionError

if __name__ == "__main__":
    test_convert()
