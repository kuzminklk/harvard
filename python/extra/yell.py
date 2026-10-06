"""
——— Source ———
From the lecture
——— Purpose ———
Example of list comprehension
"""


def main():
	yell("This", "is", "Python!")


def yell(*words):
	uppercased = [word.upper() for word in words]
	print(*uppercased)


main()
