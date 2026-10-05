import pytest

from plates import is_valid, check_length, check_start, check_numbers, check_marks


def test_complex_validity():
	assert is_valid("CS50")
	assert is_valid("AAA222")


def test_complex_invalidity():
	assert not is_valid("CS05")
	assert not is_valid("CS50P")
	assert not is_valid("PI3.14")
	assert not is_valid("H")
	assert not is_valid("OUTATIME")


def test_lenght_validity():
	assert check_length("000000")


def test_lenght_invalidity():
	assert not check_length("0000000")
	assert not check_length("0")


def test_start_validity():
	assert check_start("AA0000")
	assert check_start("BBAABB")


def test_start_invalidity():
	assert not check_start("00AABB")
	assert not check_start("A0AABB")
	assert not check_start("0AAABB")


# …
