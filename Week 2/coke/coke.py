amount=50
print(f"Amount Due: 50")
while amount > 0:
    paid=int(input("Insert Coin: "))
    if paid == 25 or paid == 10 or paid == 5:
        amount=amount-paid
        if amount > 0:
            print(f"Amount Due: {amount}")
        elif amount == 0:
            print(f"Change Owed: 0")
        else:
            print(f"Change Owed: {amount * -1}")
    else:
        print(f"Amount Due: {amount}")


