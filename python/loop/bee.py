"""
——— Source ———
From the shorts
——— Description ———
Guess the words from the letters game
——— Purpose ———
Example of dictionary methods
"""

words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
	print("Welome to Spelling Bee!")
	print("Your letters are: A I P C R H G")

	while len(words) > 0:
		print(f"{len(words)} words left!")
		guess = input("Guess a word: ")

		if guess == "GRAPHIC":
			print("Superword! You won the game!")
			words.clear()
		elif guess in words:
			points = words.pop(guess)
			print(f"Good job! You scored {points} points!")


main()
