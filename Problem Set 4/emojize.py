def main():
    inpt = input("Input: ")
    emojinize(inpt)


def emojinize(x):
    import emoji

    if ":" in x and "_" in x and x != emoji.emojize(x):
        print("Output: " + emoji.emojize(x))
    else:
        print("Output: " + emoji.emojize(x, language="alias"))


main()
