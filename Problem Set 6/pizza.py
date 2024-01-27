def main():
    response = tabularize()
    print(response)


def tabularize():
    import sys
    import csv
    from tabulate import tabulate

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            table = csv.reader(file)
            return tabulate(table, headers="firstrow", tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
