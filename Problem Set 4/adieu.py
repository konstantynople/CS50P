def main():
    adieu()


def adieu():
    import inflect

    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print("Adieu, adieu, to", p.join(names))
            break


main()
