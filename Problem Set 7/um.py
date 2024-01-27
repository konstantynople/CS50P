import re


def main():
    print(count(input("Text: ")))


def count(s):
    word = re.findall(r"\b\W*um\W*\b", s, re.IGNORECASE)
    return len(word)


if __name__ == "__main__":
    main()
