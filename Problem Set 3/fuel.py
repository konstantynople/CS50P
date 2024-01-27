def main():
    x = decimal("Fraction: ")
    print(x)


def decimal(prompt):
    while True:
        try:
            frac = input(prompt)
            x, y = frac.split("/")
            deci = int(x) / int(y)

            if deci <= 0.01:
                return "E"
            elif 0.99 <= deci <= 1:
                return "F"
            elif deci > 1:
                pass
            else:
                return f"{deci * 100:.0f}%"

        except (ValueError, ZeroDivisionError):
            pass


main()
