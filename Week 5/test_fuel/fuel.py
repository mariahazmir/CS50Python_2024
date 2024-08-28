def main():

    while True:
        fraction = input("Fraction: ")
        if "/" in fraction:
            break

    while True:
        x=round(convert(fraction))
        if x <= 100:
            break

    print(f"{gauge(x)}")


def convert(fraction):

    numerator, denominator = fraction.split("/")

    while True:
        try:
            result = int(numerator)/int(denominator)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return result * 100


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()
