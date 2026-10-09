"""
——— Source ———
From the problem set
——— Behavior ———
Prints question and asks the user for the answer, then check it and print a response
"""


def main():
	answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
	match answer:
		case "42" | "forty-two" | "forty two":
			print("Yes")
		case _:
			print("No")


main()
