"""
——— Source ———
From the problem set
——— Description ———
Omits vowels from the text
"""


def main():
	text = input("What's the text? ")
	text = omit_vowels(text)
	print(f"New text is “{text}”!")


def omit_vowels(text):
	new_text = ""
	for character in text:
		if character.lower() not in ["a", "o", "e", "i", "u"]:
			new_text += character
	return new_text


main()
