import emoji


def main():
	text = input("What's a text? ")
	text = emoji.emojize(text)
	print(text)


if __name__ == "__main__":
	main()
