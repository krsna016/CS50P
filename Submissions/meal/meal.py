def main():
    time = input("Enter time in 24-hour format: ")
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    time = time.split(":")
    min = f"{float(time[1]) / 60:.2f}"
    return int(time[0]) + float(min)


if __name__ == "__main__":
    main()
