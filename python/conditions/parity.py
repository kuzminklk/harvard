"""
——— Source ———
From the lecture
——— Behavior ———
Takes number and check if it is odd or even, then prints message
——— Purpose ———
Example of returning a Boolean value
"""


def main():
	x = int(input("What's is x? "))
	if is_even(x):
		print("X is even!")
	else:
		print("X is odd!")


def is_even(number):
	return number % 2 == 0


main()
