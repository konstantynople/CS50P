# This Python program takes any input and if it has
# emoticons of :( or :), it converts them to 🙂 or 🙁.

def main():
    inpt = input("")
    converted = convert(inpt)
    print(converted)


def convert(into):
    return into.replace(":)", "🙂").replace(":(", "🙁")


main()
