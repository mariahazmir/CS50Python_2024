import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png"]
if not any(sys.argv[1].lower().endswith(ext) for ext in valid_extensions):
    sys.exit("Invalid input")

if not sys.argv[2].split(".", -1)[-1] == sys.argv[1].split(".", -1)[-1]:
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")

fit_image = ImageOps.fit(image, shirt.size, centering=(0.5, 0.5))
fit_image.paste(shirt, shirt)
fit_image.save(sys.argv[2])
