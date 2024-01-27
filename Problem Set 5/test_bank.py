from bank import value


def main():
    test_default()
    test_payup()
    test_paymeup()


def test_default():
    assert value("Hello") == 0


def test_payup():
    assert value("Howdy") == 20
    assert value("Hey, There!") == 20


def test_paymeup():
    assert value("What's up?") == 100
    assert value("What do you want?") == 100
    assert value("0") == 100
    assert value("!") == 100


if __name__ == "__main__":
    main()
