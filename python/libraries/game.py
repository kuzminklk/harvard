"""
——— Source ———
From the problem set
——— Description ———
Guess a number game
"""

import random


def main():
	level = take_a_positive_number("What's a level? ")

	random_number = random.randint(1, level)

	while True:
		guess = take_a_positive_number("What's a guess? ")
		if guess < random_number:
			print("Too small!")
		elif guess > random_number:
			print("Too big!")
		else:
			print("Right!")
			break


def take_a_positive_number(message):
	while True:
		number = input(message)

		try:
			number = int(number)
			if number <= 0:
				print("Write a positive number!")
			else:
				return number
		except ValueError:
			print("Write a number!")


if __name__ == "__main__":
	main()
