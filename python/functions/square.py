"""
From the lecture.
Example of returning a value…
"""


def main():
	x = int(input("What's x? "))
	print(f"X squared is {square(x)}")


def square(number):
	return number**2


main()
