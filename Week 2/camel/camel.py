def main():
    name=input("camelCase: ").strip()
    if name.islower():
        print(f"snake_case: {name}")
    else:
        print(f"snake_case: {snake(name)}")

def snake(word):
    result=""
    for char in word:
        if char.isupper():
            result+="_" + char.lower()
        else:
            result+=char
    return result

main()
