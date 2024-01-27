def main():
    clean_up()


def clean_up():
    import sys
    import csv

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            with open(sys.argv[2], "w") as file:
                fields = ["first", "last", "house"]
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    writer.writerow({"first": first, "last": last,
                                    "house": student["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
