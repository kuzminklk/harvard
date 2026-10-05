import inflect
from datetime import date


def main():
	"""Take birth date in ISO 8601 format, then calculate and print amount of minutes passed since in words"""
	today = date.today()
	birth_date = input("What's your birth date? ").strip()

	try:
		birth_date = date.fromisoformat(birth_date)
	except ValueError:
		print("Invalid input")

	difference = today - birth_date
	print(convert(difference))


def convert(difference):
	"Convert the date difference to minutes represented in words"
	minutes = int(difference.total_seconds() / 60)
	# Use “inflect” to turn minutes into words
	engine = inflect.engine()
	minutes_in_words = engine.number_to_words(minutes)

	return minutes_in_words.title()


if __name__ == "__main__":
	main()
