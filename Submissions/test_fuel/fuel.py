import sys


def main():
    input_ = input()
    perc = convert(input_)
    print(gauge(perc))


def convert(fraction):
    if fraction.count("/") != 1:
        raise ValueError

    a, b = fraction.split("/")

    if not a.isdigit() or not b.isdigit():
        raise ValueError
    elif b == "0":
        raise ZeroDivisionError
    elif int(a) > int(b):
        raise ValueError
    c = (int(a) / int(b)) * 100
    return round(c)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
