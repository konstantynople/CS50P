from plates import is_valid


def main():
    test_default()
    test_invalid()


def test_default():
    # Testing for 2-6 characters, starting with 2 letters
    assert is_valid("CS") is True
    assert is_valid("CS50") is True
    assert is_valid("BEST50") is True


def test_invalid():
    # Testing for all corner cases where program is False
    assert is_valid("50") is False
    assert is_valid("C5") is False
    assert is_valid("THISISCS50") is False
    assert is_valid("CS05") is False
    assert is_valid("CS50P") is False
    assert is_valid("PI3.14") is False
    assert is_valid("H") is False
    assert is_valid("OUTATIME") is False
    assert is_valid("123456") is False
    assert is_valid("CS05P") is False


if __name__ == "__main__":
    main()
