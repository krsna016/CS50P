import csv
import sys
import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        make_table(sys.argv[1])


def make_table(string):
    lists = []
    try:
        with open(string) as file:
            for line in file:
                line = line.strip()
                lists.append(line.split(","))
    except FileNotFoundError:
        sys.exit("File does not exists")
    else:
        print(tabulate.tabulate(lists,headers="firstrow",tablefmt="grid"))


if __name__ == "__main__":
    main()
