"""
——— Source ———
From the lecture
——— Purpose ———
Example of “yield”
"""


def main():
	amount = int("How much? ")
	for sheep in sheeps(amount):
		print(sheep)


def sheeps(amount):
	for index in range(amount):
		yield "🐑" * index


main()
