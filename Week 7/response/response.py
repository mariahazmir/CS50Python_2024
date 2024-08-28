import validators

email = input("What's your email address? ")

if validators.email(email):
    print(f"Valid")
else:
    print(f"Invalid")
