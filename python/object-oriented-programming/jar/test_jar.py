import pytest

from jar import Jar


def test_init():
	jar = Jar(5)
	assert jar.capacity == 5


def test_str():
	jar = Jar(5)
	jar.deposit(5)
	assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
	jar = Jar(5)
	jar.deposit(5)
	assert jar.size == 5

	with pytest.raises(ValueError):
		jar.deposit(1)


def test_withdraw():
	jar = Jar(5)
	jar.deposit(5)
	jar.withdraw(1)
	assert jar.size == 4

	with pytest.raises(ValueError):
		jar.withdraw(5)
