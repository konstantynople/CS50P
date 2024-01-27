from numb3rs import validate


def main():
    test_default()
    test_invalid()


def test_default():
    assert validate("1.2.3.4") is True
    assert validate("12.23.34.45") is True
    assert validate("255.255.255.255") is True


def test_invalid():
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.5555") is False
    assert validate("-1.1.2.3") is False
    assert validate("76.512.255.12") is False
    assert validate("cat") is False


if __name__ == "__main__":
    main()
