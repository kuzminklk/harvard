"""
From the problem set.
Take user input and change all spaces to “…”, then print the message.
"""


def main():
	message = input("Write an message: ")
	message = message.replace(" ", "…")
	print(message)


main()
