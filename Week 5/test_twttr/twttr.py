def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    result = ""
    for char in word:
        match char:
            case "A" | "E" | "I" | "O" | "U" | "a" | "e" | "i" | "o" | "u" :
                result+=""
            case _:
                result+=char
    return result


if __name__ == "__main__":
    main()
