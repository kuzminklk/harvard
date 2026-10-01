import pytest

from .fuel import turn_to_percentage


def test_turn_to_percentage_value_error():
	with pytest.raises(ValueError):
		turn_to_percentage("What?")


def test_turn_to_percentage_zero_division_error():
	with pytest.raises(ZeroDivisionError):
		turn_to_percentage("0/0")
