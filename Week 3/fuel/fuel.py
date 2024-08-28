def main():

    while True:
        x=round(get_percentage())
        if x <= 100:
            break

    if x <= 1:
        print(f"E")
    elif x >= 99:
        print(f"F")
    else:
        print(f"{x}%")

def get_percentage():

    while True:
        fraction = input("Fraction: ")
        if "/" in fraction:
            break

    numerator, denominator = fraction.split("/")

    while True:
        try:
            result = int(numerator)/int(denominator)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return result * 100

main()
