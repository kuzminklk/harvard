"""
——— Source ———
From the problem set
——— Description ———
Turns fractionated fuel into percentage
"""


def main():
	percentage = get_fraction_and_turn_to_percentage("What's fraction? ")
	print_fuel_amount(percentage)


def get_fraction_and_turn_to_percentage(message):
	while True:
		fraction = input(message).strip()
		x, y = fraction.split("/")
		try:
			x = float(x)
			y = float(y)
			if x > y:
				print("First value of a fraction must be lesser, than second")
			else:
				return x / y * 100
		except ValueError:
			print("Fraction must be written like “3/4”")
		except ZeroDivisionError:
			print("Second value of a fraction must be not 0")


def print_fuel_amount(percentage):
	message = None

	if percentage > 99:
		message = "F"
	elif percentage < 1:
		message = "E"

	if message:
		print(message)
	else:
		print(f"{percentage:.0f}%")


main()
