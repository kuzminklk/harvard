import pytest

from ip import validate


def test_validity():
	assert validate("123.1.1.32")
	assert validate("123.1.1.222")
	assert validate("0.0.0.11")


def test_invalidity():
	assert not validate("566.1.1.32")
	assert not validate("123.1.464.222")
	assert not validate("sdf.0.0.11fsddf")
