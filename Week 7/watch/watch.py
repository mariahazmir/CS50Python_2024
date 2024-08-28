import re


def main():
    print(parse(input("HTML: ")).strip())


def parse(s):
    matches = re.search(r"^(.+)?(http)(.+)(embed/)(.+)(\")(.+)?$", s)
    if matches:
        link = matches.group(5)
        return(f"https://youtu.be/{link}")
    else:
        return(f"None")

if __name__ == "__main__":
    main()
