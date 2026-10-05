"""
——— Source ———
From the lecture
——— Purpose ———
Example of class method…
"""

import random


class Hat:
	houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

	@classmethod
	def sort(cls, name):
		print(f"{name} is in {random.choice(cls.houses)}")


def main():
	Hat.sort("Harry")


if __name__ == "__main__":
	main()
