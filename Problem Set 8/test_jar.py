from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)

    jar = Jar(10)
    assert str(jar) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.deposit(13)

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(1)

    jar.deposit(12)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
