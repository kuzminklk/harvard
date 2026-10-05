def main():
	percentage = get_fraction_and_turn_to_percentage("What's fraction? ")
	print_fuel_amount(percentage)


def get_fraction_and_turn_to_percentage(message):
	while True:
		fraction = input(message).strip()
		return turn_to_percentage(fraction)


def turn_to_percentage(fraction):
	x, y = fraction.split("/")
	x = float(x)
	y = float(y)
	if x > y:
		print("First value of a fraction must be lesser, than second")
	else:
		return (x / y) * 100


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


if __name__ == "__main__":
	main()
