"""
——— Source ———
From the lecture
——— Behavior ———
Takes user input and select appropriate house for the name
——— Purpose ———
Example of “match” conditional operator
"""


def main():
	name = input("What's your name? ")

	match name:
		case "Harry" | "Hemione" | "Ron":
			print("Gryffindor")
		case "Draco":
			print("Slytherin")
		case _:
			print("Who?")


main()
