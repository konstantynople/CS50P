def main():
    inpt = input("Input: ")
    print(shorten(inpt))


def shorten(str):

    new_str = ""

    for i in str:
        match i:
            case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
                next
            case _:
                new_str += i

    return new_str


if __name__ == "__main__":
    main()
