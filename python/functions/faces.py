"""
From the problem set.
Take user input and change emojicons like “(:” to appropriate emoji (🙂), then print the result.
"""


def main():
	message = input("Write an message: ")
	message = convert(message)
	print(message)


def convert(text):
	text = text.replace("(:", "🙂")
	text = text.replace(":)", "🙂")
	text = text.replace("):", "🙁")
	text = text.replace(":(", "🙁")
	return text


main()
