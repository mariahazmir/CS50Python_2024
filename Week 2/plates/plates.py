def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6 and s.isalnum()):
        return False
    if not s[:2].isalpha():
        return False
    end_letter = False
    for i in s:
        if i.isdigit():
            if i == "0" and not end_letter:
                return False
            end_letter = True
        elif end_letter:
            return False
    return True

main()
