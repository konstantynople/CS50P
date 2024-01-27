from validator_collection import validators


def main():
    print(validation(input("What's your email address? ")))


def validation(inpt):
    try:
        if validators.email(inpt):
            return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
