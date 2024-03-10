import csv
import pprint
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and (not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")
    else:
        read_file(sys.argv[1])


def read_file(read_from):
    lists = []
    try:
        with open(read_from) as file:
            reader = csv.DictReader(file)
            for line in reader:
                lists.append(line)
    except FileNotFoundError:
        sys.exit(f"Could not read {read_from}")
    else:
        write_file(lists)


def write_file(a_list):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first" : "first","last":"last","house":"house"})
        for line in a_list:
            writer.writerow({
                "house": line["house"],
                "first": (line["name"].split(","))[1].strip(),
                "last": (line["name"].split(","))[0]
            })


if __name__ == "__main__":
    main()
