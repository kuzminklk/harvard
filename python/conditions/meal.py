"""
——— Source ———
From the problem set
——— Behavior ———
Asks for the time, then select a meal if it's the time
"""


def main():
	time = input("What's the time? ")
	time = time.strip().lower()
	hours = convert(time)
	meal = select_a_meal(hours)
	if meal is not None:
		print(f"It's {meal} time!")


def convert(time):
	hours, minutes = time.split(":")
	hours = float(hours)
	minutes = float(minutes)
	hours = hours + (minutes / 60)
	return hours


def select_a_meal(hours):
	if 7 <= hours <= 8:
		return "breakfast"
	elif 12 <= hours <= 13:
		return "lunch"
	elif 18 <= hours <= 19:
		return "dinner"


if __name__ == "__main__":
	main()
