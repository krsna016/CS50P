from PIL import Image, ImageOps
import sys


def main():
    # Input File : before1.jpg
    # Output File : after1.jpg
    extensions = ["jpg", "jpeg", "png"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and (not (sys.argv[1][-3:] == sys.argv[2][-3:])):
        sys.exit("Input and output have different extensions")
    elif sys.argv[1][-3:] not in extensions:
        sys.exit("Invalid output")
    else:
        overlay(sys.argv[1])


def overlay(argument):
    overlay_image = Image.open("shirt.png")
    base_image = Image.open(sys.argv[1])
    try:
        with Image.open(sys.argv[1]) as image:
            cropped = ImageOps.fit(base_image, overlay_image.size)
            cropped.paste(overlay_image, mask=overlay_image)
            cropped.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
