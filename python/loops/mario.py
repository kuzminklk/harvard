"""
——— Source ———
From the lecture
——— Behavior ———
Prints square from little square symbols
——— Purpose ———
Example of loops and logic decomposing to functions
"""


def main():
	print_square(10)


def print_square(size):
	for i in range(size):
		print_row(size * 2)  # Multiply by 2 to align visually in the terminal


def print_row(width):
	print("■" * width)


main()
