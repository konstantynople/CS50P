from datetime import date
import inflect
import operator
import sys

p = inflect.engine()


def main():
    print(days_convert(input("Date of Birth: ")))


def days_convert(DOB):
    try:
        dayz = operator.sub(date.today(), date.fromisoformat(DOB)).days
        return f"{mins_convert(dayz)} minutes"
    except ValueError:
        sys.exit("Invalid date")


def mins_convert(days):
    minutes = days * 24 * 60
    return p.number_to_words(minutes, andword=" ").capitalize()


if __name__ == "__main__":
    main()
