import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    value = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

rate = response.json()

usd_rate = float(rate["bpi"]["USD"]["rate_float"])

price = usd_rate * value

print(f"${price:,}")
