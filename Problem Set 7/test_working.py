import pytest
from working import convert


def main():
    test_default()
    test_invalid()


def test_default():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("10 PM to 9 AM") == "22:00 to 09:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("cat and dog")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()
