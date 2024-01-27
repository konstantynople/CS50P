def main():
    camelCase = input("camelCase: ")
    snakecase(camelCase)


def snakecase(str):
    # Creates an empty list
    res = ""

    # Check each character in a string
    for i in str:
        # If the character is uppercase, then it'll add
        # underscore, lowercase it, and add it to a new string.
        if i.isupper():
            res += "_" + i.lower()
        # If the character is already lowercase, and it to a
        # new string.
        else:
            res += i

    print(res)


main()
