"""
——— Source ———
From the problem set
——— Description ———
Turns camel case variables name into snake case
"""


def main():
	name = input("What's the name? ")
	name = turn_to_snake_case(name)
	print(f"New name is: {name}!")


def turn_to_snake_case(name):
	snake_case_name = ""
	for character in name:
		if character.isupper():
			snake_case_name += "_" + character.lower()
		else:
			snake_case_name += character
	return snake_case_name


main()
