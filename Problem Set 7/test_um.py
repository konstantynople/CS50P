from um import count


def main():
    test_default()
    test_invalid()


def test_default():
    assert count("Um?") == 1
    assert count("Sorry, um, for, um, bothering, um, you") == 3
    assert count("Hello, um, world, um") == 2


def test_invalid():
    assert count("Dumpster") == 0
    assert count("Trumbone") == 0


if __name__ == "__main__":
    main()
