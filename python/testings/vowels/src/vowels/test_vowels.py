import pytest

from .vowels import omit_vowels


def test_omiting():
	text = "Hello! What's up?"
	text_with_omitted_vowels = omit_vowels(text)
	example = "Hll! Wht's p?"
	assert text_with_omitted_vowels == example
