import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(0?[1-9]|1[0-2])(:[0-5][0-9])? ([AMPM]{2}) to (0?[1-9]|1[0-2])(:[0-5][0-9])? ([AMPM]{2})"

    if matches := re.search(regex,s):
        
        if matches.group(3) == "AM":
            time_1 = int(matches.group(1))
            if time_1 == 12:
                time_1 = 0
        else:
            if int(matches.group(1)) == 12:
                time_1 = 12
            else:
                time_1 = int(matches.group(1)) + 12

        if matches.group(6) == "AM":
            time_3 = int(matches.group(4))
            if time_3 == 12:
                time_3 = 0
        else:
            if int(matches.group(4)) == 12:
                time_3 = 12
            else:
                time_3 = int(matches.group(4)) + 12

        if matches.group(2):
            time_2 = matches.group(2)
        else:
            time_2 = ":00"

        if matches.group(5):
            time_4 = matches.group(5)
        else:
            time_4 = ":00"

        return f"{time_1:02}{time_2} to {time_3:02}{time_4}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()



