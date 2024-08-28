import sys
from pyfiglet import Figlet

figlet=Figlet()

if len(sys.argv) != 3:
    sys.exit("Invalid usage")

if sys.argv[2] in figlet.getFonts() and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

print(f"Output: {figlet.renderText(input("Input: "))}")
