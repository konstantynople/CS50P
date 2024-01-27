def main():
    funkytext()


def funkytext():
    import sys
    from pyfiglet import Figlet
    from random import choice

    figlet = Figlet()
    print(sys.argv[2])

    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(text))
    elif len(sys.argv) > 2 and ("-f" in sys.argv or "--f" in sys.argv):
        if sys.argv[2] in figlet.getFonts():
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) > 2 and ("-f" not in sys.argv or "--f" not in sys.argv):
        sys.exit("Invalid usage")
    else:
        sys.exit("Invalud usage")


main()
