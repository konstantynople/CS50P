def main():
    guessing_game()


def guessing_game():
    import random

    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                pass
            elif guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
