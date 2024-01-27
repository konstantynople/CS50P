import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r"^<iframe.*https?.*youtube\.com/embed(/xvFZjo5PgG0).*></iframe>$", s
    ):
        return f"https://youtu.be{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
