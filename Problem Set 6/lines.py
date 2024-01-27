def main():
    response = line_counter()
    print(response)


def line_counter():
    import sys

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

    try:
        line_count = 0

        with open(sys.argv[1]) as file:
            lines = file.readlines()
            for line in lines:
                if line.lstrip().startswith("#") or line.strip() == "":
                    continue
                else:
                    line_count += 1
            return line_count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
