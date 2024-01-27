import random


def main():
    number = get_level()
    score = 0

    for _ in range(10):
        errors = 0
        value_1 = generate_integer(number)
        value_2 = generate_integer(number)

        while True:
            answer = int(input(f"{value_1} + {value_2} = "))

            if value_1 + value_2 == answer:
                score += 1
                break
            else:
                print("EEE")
                errors += 1
                if errors == 3:
                    print(f"{value_1} + {value_2} = {value_1 + value_2}")
                    break
                pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 0 < level < 4:
                return level
            else:
                pass

        except ValueError:
            pass


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
