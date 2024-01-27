def main():
    num = convert(input("Fraction: "))
    print(gauge(num))


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) / int(y) > 1:
        raise ValueError
    else:
        return int(x) / int(y) * 100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif percentage > 100:
        raise ValueError
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
