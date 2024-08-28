import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

i = 0

for line in lines:
    stripped_line = line.strip()
    if stripped_line and not stripped_line.startswith("#"):
        i += 1

print(i)
