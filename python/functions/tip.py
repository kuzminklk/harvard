"""
——— Source ———
From the problem set
——— Behavior ———
Takes user input, calculates the tip, prints appropriate message
"""


def main():
	dollars = dollars_to_float(input("How much was the meal? "))
	percent = percent_to_float(input("What percentage would you like to tip? "))
	tip = dollars * percent
	print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
	dollars = dollars.removeprefix("$")
	return float(dollars)


def percent_to_float(percent):
	percent = percent.removesuffix("%")
	return float(percent) / 100


main()
