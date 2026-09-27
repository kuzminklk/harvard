"""
——— Source ———
From the problem set
——— Behavior ———
Takes user input and changes all spaces to “…”, then prints the message
"""


def main():
	message = input("Write an message: ")
	message = message.replace(" ", "…")
	print(message)


main()
