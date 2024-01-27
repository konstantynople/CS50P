def main():
    greet = input("Greeting: ")
    money = value(greet)
    print(f"${money}")


def value(greeting):
    first_word = greeting.split()[0].lower().strip().replace(",", "")

    if first_word == "hello":
        return 0
    elif first_word[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
