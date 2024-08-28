word=input("Input: ")
result=""
for char in word:
    match char:
        case "A" | "E" | "I" | "O" | "U" | "a" | "e" | "i" | "o" | "u" :
            result+=""
        case _:
            result+=char
print(f"Output: {result}")
