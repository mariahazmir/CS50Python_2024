import re
from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        dob = validate(input("Date of Birth: "))
        total_minutes = calculate_minutes(dob)
        words = convert_number(total_minutes)
        print(f"{words} minutes")
    except ValueError:
        print("Invalid date.")
        sys.exit(1)

def validate(s):
    if re.search(r'^\d{4}-\d{2}-\d{2}$', s):
        return date.fromisoformat(s)
    else:
        raise ValueError

def calculate_minutes(past_date):
    now = date.today()
    difference = (now - past_date).total_seconds() // 60
    return int(difference)

def convert_number(number):
    return p.number_to_words(number, andword="").capitalize()

if __name__ == "__main__":
    main()
