import emoji


def main():
    i = input("Input: ")
    print(f"Output: {emoji.emojize(i, language='alias')}")


if __name__ == "__main__":
    main()
