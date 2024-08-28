import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

x, y, z = input("Expression: ").split(" ")
ans = operators[y](float(x), float(z))
print(f"{ans}")
