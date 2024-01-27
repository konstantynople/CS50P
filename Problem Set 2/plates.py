def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if 2 <= len(s) <= 6 and s.isalnum():

        if s.isalpha():
            return True

        else:

            while s[i].isalpha():
                i += 1

                if i == 6:
                    break

            else:

                if s[0:i-1].isalpha() and s[i:].isdigit() and s[i] != "0":
                    pass
                else:
                    return False

    else:
        return False

    return True


main()
