"""
——— Source ———
From the lecture
——— Description ———
Shuffles cards
"""

import random


def main():
	cards = ["Jack", "Queen", "King"]
	random.shuffle(cards)
	for card in cards:
		print(card)


main()
