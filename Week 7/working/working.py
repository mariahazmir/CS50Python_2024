import re

def main():
    
    print(convert(input("Hours: ")).strip())

def convert(s):

    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s)

    if matches:
        hourB = int(matches.group(1))
        minB = int(matches.group(2) or 0)
        hourA = int(matches.group(4))
        minA = int(matches.group(5) or 0)

        if hourA > 12 or hourB > 12 or minA >= 60 or minB >= 60:
            raise ValueError

        if matches.group(3) == "PM" and hourB != 12:
            hourB += 12
        elif matches.group(3) == "AM" and hourB == 12:
            hourB = 0

        if matches.group(6) == "PM" and hourA != 12:
            hourA += 12
        elif matches.group(6) == "AM" and hourA == 12:
            hourA = 0

        return f"{hourB:02}:{minB:02} to {hourA:02}:{minA:02}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
