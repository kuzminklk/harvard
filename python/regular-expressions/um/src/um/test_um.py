import pytest

from .um import count


def test_count():
	assert count("um") == 1
	assert count("Um") == 1
	assert count("UM") == 1
	assert count("um, um, um") == 3
	assert count("ummm") == 0
	assert count("um?") == 1
	assert count("um!") == 1
	assert count("um.") == 1
	assert count("um,") == 1
	assert count("um;") == 1
	assert count("um:") == 1
	assert count("um'") == 1
	assert count('um"') == 1
	assert count("um-") == 1
	assert count("um/") == 1
	assert count("um\\") == 1
	assert count("um|") == 1
	assert count("um~") == 1


def test_count_not_count_word():
	assert count("umbrella") == 0
	assert count("humble") == 0
	assert count("thumb") == 0
