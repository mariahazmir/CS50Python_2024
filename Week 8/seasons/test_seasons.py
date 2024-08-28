import unittest
from datetime import date
import inflect
from seasons import validate, calculate_minutes, convert_number

class TestDateFunctions(unittest.TestCase):

    def setUp(self):
        self.p = inflect.engine()

    def test_validate_valid_date(self):
        self.assertEqual(validate("2023-08-01"), date(2023, 8, 1))

    def test_validate_invalid_date(self):
        with self.assertRaises(ValueError):
            validate("01-08-2023")
        with self.assertRaises(ValueError):
            validate("2023/08/01")
        with self.assertRaises(ValueError):
            validate("2023-02-30")

    def test_calculate_minutes(self):
        past_date = date(2023, 8, 1)
        today = date.today()
        expected_minutes = int((today - past_date).total_seconds() // 60)
        self.assertEqual(calculate_minutes(past_date), expected_minutes)

    def test_convert_number(self):
        self.assertEqual(convert_number(0), "Zero")
        self.assertEqual(convert_number(1), "One")
        self.assertEqual(convert_number(525600), "Five hundred twenty-five thousand, six hundred")
        self.assertEqual(convert_number(1234567), "One million, two hundred thirty-four thousand, five hundred sixty-seven")

if __name__ == "__main__":
    unittest.main()
