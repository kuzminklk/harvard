"""
——— Source ———
From the problem set
——— Description ———
Takes coins and counts amount due
"""


def main():
	amount = 50
	while amount > 0:
		print(f"Amount due: {amount}")
		insertion = int(input("Insert a coin: "))
		if insertion == 50 or insertion == 25 or insertion == 10 or insertion == 5:
			amount -= insertion


main()
