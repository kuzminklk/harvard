"""
——— Source ———
From the lecture
——— Purpose ———
Example of: functions, variables, program flow, concatenations, formatted strings, detached main function convention
"""


def main():
	greet()


def greet():
	# Ask for the name
	name = input("What's your name? ")

	# Remove whitespaces from the left and from the right
	name = name.strip()

	# Capitalize user's name
	name = name.title()

	"""
	Or combine together
	name = input("What's your name? ").strip().title()
	"""

	# Extract first name
	firstName, lastName = name.split(" ")

	# Greet the user
	print(f"Hello, {firstName}!")


main()
