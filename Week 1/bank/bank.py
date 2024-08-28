greeting=input("Greeting: ").strip().lower()
if greeting.startswith("hello"):
    print(f"$0")
elif greeting.startswith("h"):
    print(f"$20")
else:
    print(f"$100")
