from um import count
import sys

def test_count():
    try:
        assert count("um") == 1
        assert count("um, hello") == 1
        assert count("hello um") == 1
        assert count("I said um twice, um.") == 2
        assert count("umbrella") == 0
        assert count("Um, I think um, you mean um.") == 3
        assert count("There is no match here.") == 0
        assert count("UM, um, uM, Um.") == 4

    except AssertionError:
        sys.exit(1)

if __name__ == "__main__":
    test_count()
