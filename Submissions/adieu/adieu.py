import inflect
import sys


def main():
    names = []
    p = inflect.engine()
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break
    names_str = p.join(names)
    print(f"Adieu, adieu, to {names_str}")


if __name__ == "__main__":
    main()
