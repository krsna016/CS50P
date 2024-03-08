def main():
    while True:
        try:
            gauge = input("Fraction: ")
            a,b = gauge.split("/")
            a = int(a)
            b = int(b)
            c = (int(a)/int(b)) * 100
            if (a > b):
                continue
            elif c >= 99:
                print("F")
                break
            elif c <= 1:
                print("E")
                break
            else:
                print(f"{round(c)}%")
                break
        except (ZeroDivisionError, ValueError):
            pass


if __name__ == "__main__":
    main()
