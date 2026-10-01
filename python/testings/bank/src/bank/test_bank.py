import pytest

from .bank import choose_value


def test_wrong_greeting():
	greeting = "As-salamu alaykum!"
	value = choose_value(greeting)
	assert value == 100


def test_particularly_right_greeting():
	greeting = "Hey!"
	value = choose_value(greeting)
	assert value == 20


def test_right_greeting():
	greeting = "Hello!"
	value = choose_value(greeting)
	assert value == 0
