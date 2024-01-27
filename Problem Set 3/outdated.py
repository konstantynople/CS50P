def main():
    x = standardized_date("Date: ")
    print(x)


def standardized_date(prompt):
    month_name = [
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
            date = input(prompt)

            if ", " in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                if month in month_name:
                    month = month_name.index(month) + 1
                    day = int(day)
                    year = int(year)
            else:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            if month < 12 and day < 31:
                return f"{year}-{month:02}-{day:02}"

        except (TypeError, ValueError):
            pass


main()
