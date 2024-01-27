def main():
    inpt = input("Input: ")
    vowel_omitter(inpt)


def vowel_omitter(str):

    new_str = ""

    for i in str:
        match i:
            case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
                next
            case _:
                new_str += i

    print(f"Output: {new_str}")


main()
