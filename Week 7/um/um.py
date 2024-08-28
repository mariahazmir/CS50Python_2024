import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    ums = re.findall(r'\bum\b', s, re.IGNORECASE)
    for um in ums:
        counter += 1
    return counter

if __name__ == "__main__":
    main()
