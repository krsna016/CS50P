import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        print_lines(sys.argv[1])


def print_lines(file_path):
    total_lines = 0
    try:
        with open(file_path) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        for line in lines:
            if line.lstrip().startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                total_lines += 1
        print(total_lines)


if __name__ == "__main__":
    main()