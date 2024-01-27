from twttr import shorten


def main():
    test_default()
    test_argument()
    test_characters()


def test_default():
    assert shorten("") == ""


def test_argument():
    assert shorten("Stan") == "Stn"
    assert shorten("Gorge") == "Grg"
    assert shorten("Kostyantyn Alexander Luferov") == "Kstyntyn lxndr Lfrv"


def test_characters():
    assert shorten("0") == "0"
    assert shorten("!") == "!"


if __name__ == "__main__":
    main()
