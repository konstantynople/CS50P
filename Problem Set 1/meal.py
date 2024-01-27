def main():
    inpt = input("What time is it? ").lower()

    tim = convert(inpt)

    if 7 <= tim <= 8:
        print("breakfast time")
    elif 12 <= tim <= 13:
        print("lunch time")
    elif 18 <= tim <= 19:
        print("dinner time")


def convert(time):
    if "p.m." in time:
        hours, minutes = time.split()[0].split(":")
        return int(hours) + 12 + int(minutes)/60
    else:
        hours, minutes = time.split()[0].split(":")
        return int(hours) + int(minutes)/60


if __name__ == "__main__":
    main()
