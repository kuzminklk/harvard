"""
——— Source ———
From the lecture
——— Behavior ———
Takes two numbers from the user and compares them, then print the result
——— Purpose ———
Example of conditional operator
"""


def main():
	x = int(input("What's x? "))
	y = int(input("What's y? "))
	if x == y:
		print("x is equal to y")
	else:
		print("x is not equal to y")


main()
