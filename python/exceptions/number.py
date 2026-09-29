"""
——— Source ———
From the lecture
——— Purpose ———
Example of handling exceptions
"""


def main():
	x = get_integer("What's x? ")
	print(f"X is {x}")


def get_integer(message):
	while True:
		try:
			return int(input(message))
		except ValueError:
			pass


main()
