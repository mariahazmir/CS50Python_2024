def main():
    time=convert(input("What time is it? ").strip())
    if 6.5 < time < 10:
        print(f"breakfast time")
    elif 12 < time < 14:
        print(f"lunch time")
    elif 17 < time < 21:
        print(f"dinner time")

def convert(time):
    hours, minutes = time.split(":")
    mins = float(minutes)/60
    return float(hours) + float(mins)


if __name__ == "__main__":
    main()
