from numb3rs import validate

def test_validate():
    test_cases = [
        ("192.168.1.1", True),
        ("255.255.255.255", True),
        ("0.0.0.0", True),
        ("127.0.0.1", True),
        ("256.256.256.256", False),
        ("192.168.1.256", False),
        ("192.168.1", False),
        ("192.168.1.1.1", False),
        ("192.168..1", False),
        ("abc.def.ghi.jkl", False),
        ("1234.123.123.123", False)
    ]

    for ip, expected in test_cases:
        assert validate(ip) == expected

if __name__ == "__main__":
    test_validate()
