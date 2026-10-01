"""
——— Source ———
From the problem set
——— Description ———
Education game
"""

import random


def main():
	while True:
		level = take_a_positive_number("What's a level? ")
		if level in [1, 2, 3]:
			break
		else:
			print("Choose between: 1, 2, or 3 level")

	generate_problems(level)


def generate_problems(level):
	score = 0
	task = 0

	while task < 10:
		x = random.randint(0, 10**level)
		y = random.randint(0, 10**level)

		tries = 0
		while tries < 3:
			z = take_a_positive_number(f"{x} + {y} = ")
			if x + y == z:
				score += 1
				break
			elif tries == 2:
				print(f"{x} + {y} = {z}")
			else:
				print("Error!")

		task += 1

	print(f"Your score is {score}")


def take_a_positive_number(message):
	while True:
		number = input(message).strip()

		try:
			number = int(number)
			if number < 0:
				print("Write a positive number!")
			else:
				return number
		except ValueError:
			print("Write a number!")


if __name__ == "__main__":
	main()
