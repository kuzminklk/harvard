"""
——— Source ———
From the lecture and particularly on my own
——— Purpose ———
Example of unpacking positional function arguments
"""

names = ["Harry", "Ron", "Draco"]


def say_hello(*names):
	for name in names:
		print(f"Hello {name}!")


say_hello(*names)
