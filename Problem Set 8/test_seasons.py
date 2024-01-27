import pytest
from seasons import mins_convert


def main():
    test_default()


def test_default():
    assert (
        mins_convert(126572)
        == "One hundred eighty-two million, two hundred sixty-three thousand, six hundred eighty"
    )
    assert mins_convert(26) == "Thirty-seven thousand, four hundred forty"


if __name__ == "__main__":
    main()
