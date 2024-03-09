from pyfiglet import Figlet
import sys


class FontNotFound(Exception):
    pass


def main():
    figlet = Figlet()
    try:
        if sys.argv[1] != "-f":
            raise FontNotFound
        if sys.argv[2] not in figlet.getFonts():
            raise FontNotFound
    except FontNotFound:
        sys.exit("Invalid usage")


    strs = input("Input: ")
    # If user not give any command line arguments: eg: python figlet.py, then print the default font
    if len(sys.argv) == 1:
        print(figlet.renderText(strs))
    # User given two command line argument: eg: python figlet.py -f slant, then print the font which user given
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(strs))


if __name__ == "__main__":
    main()
