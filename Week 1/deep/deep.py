answer=input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
match answer:
    case "42" | "forty-two" | "forty two":
        print(f"Yes")
    case _:
        print(f"No")
