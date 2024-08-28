import random


def main():
    level = get_level()
    points = 0
    for i in range(10):
        x, y = generate_integer(level)
        correct = x + y
        answer = int(input(f"{x} + {y} = "))
        if correct != answer:
            j = 0
            while j < 3:
                if j == 2:
                    print(f"EEE\n{x} + {y} = {correct}")
                else:
                    print(f"EEE")
                    answer = input(f"{x} + {y} = ")
                j = j+1
        else:
            points = points + 1

    print(f"Score: {points}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= n <= 3:
                return n


def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    else:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)

    return X, Y


if __name__ == "__main__":
    main()
