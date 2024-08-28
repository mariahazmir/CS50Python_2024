import inflect

p = inflect.engine()

list = []

while True:
    try:
        name = input("Name: ").title().strip()
    except EOFError:
        print()
        break
    else:
        if not name:
            break
        list.append(name)

print(f"Adieu, adieu, to {p.join(list)}")
