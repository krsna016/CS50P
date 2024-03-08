def main():
    n = int(input("Enter the height : "))
    pyramid(n)


def pyramid(height):
    for i in range(height):
        print(". " * (height - i - 1), end="")
        print("# " * (i + 1))


if __name__ == "__main__":
    main()
