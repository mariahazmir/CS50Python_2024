def convert(face):
    return face.replace(":)", "🙂").replace(":(", "🙁")

def main():
    print(f"{convert(input())}")

main()
