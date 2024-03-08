class InvalidDateError(Exception):
    pass


def main():
    day = month = year = ""
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date : ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                if month.isalpha():
                    raise InvalidDateError
            elif "," in date:
                month, day, year = date.split(" ")
                month = month.title()
                day = day.replace(",", "")
            elif " " in date:
                day, month, year = date.split(" ")
                month = month.title()

            if int(day) > 31:
                raise InvalidDateError
            if month.isalpha():
                if month not in months:
                    raise InvalidDateError
            if month.isdigit():
                if int(month) > 12:
                    raise InvalidDateError

        except (InvalidDateError, ValueError):
            pass
        else:
            if month.isdigit():
                formatted_month = month.zfill(2) if 1 <= int(month) <= 9 else month
                formatted_day = day.zfill(2) if 1 <= int(day) <= 9 else day
                print(f"{year}-{formatted_month}-{formatted_day}")
            else:
                formatted_month = str(months.index(month) + 1).zfill(2) if 1 <= (months.index(month) + 1) <= 9 else (
                            months.index(month) + 1)
                formatted_day = day.zfill(2) if 1 <= int(day) <= 9 else day
                print(f"{year}-{formatted_month}-{formatted_day}")
            break


if __name__ == "__main__":
    main()
