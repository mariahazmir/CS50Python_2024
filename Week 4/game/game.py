import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n >= 1:
            break

number = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > 0:
            break

while guess != number:
    if guess < number:
        print(f"Too small!")
    elif guess > number:
        print(f"Too large!")

print(f"Just right!")
