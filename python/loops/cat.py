"""
——— Source ———
From the lecture
——— Behavior ———
Asks for the number of meows, then meows such times
——— Purpose ———
Example of loops and list (from “range()”)
"""


def main():
	number = get_positive_number()
	meow(number)


def get_positive_number():
	while True:
		number = int(input("What's a number of meows? "))
		if number > 0:
			return number


def meow(quantity):
	for _ in range(quantity):
		print("meow 🐈", end=" ")


main()
