def main():
    groceries = grocery_list("")
    for key, value in sorted(groceries.items()):
        print(f"{value} {key}")


def grocery_list(prompt):
    dictionary = {}

    while True:
        try:
            item = input(prompt).upper()
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
        except EOFError:
            return dictionary


main()
