import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            last, first = row["name"].split(", ")
            rows.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

try:
    with open(sys.argv[2], "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)
except Exception as e:
    sys.exit(f"Error writing to file: {e}")
