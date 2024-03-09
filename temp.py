def main():
    input_ = input()
    perc = convert(input_)
    gauge(perc)


def convert(fraction):
    a, b = fraction.split("/")
    if not a.isdigit() or not b.isdigit() or int(a) > int(b):
        raise ValueError
    if b == "0":
        raise ZeroDivisionError
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
