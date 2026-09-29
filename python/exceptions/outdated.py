"""
——— Source ———
From the problem set
——— Description ———
Turn one date format into another
"""

MOUNTHS = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December",
]


def main():
	year, mounth, day = input_a_date("What's a date? ")
	print(f"{year:04}-{mounth:02}-{day:02}")


def input_a_date(message):
	while True:
		date = input(message).strip().title()
		try:
			if date.count("/") == 2:
				mounth, day, year = date.split("/")
				mounth = int(mounth)
				day = int(day)
				year = int(year)
				return year, mounth, day
			else:
				mounth, day, year = date.split(" ")
				mounth = MOUNTHS.index(mounth)
				day = int(day[:-1])
				year = int(year)
				return year, mounth, day
		except ValueError:
			print("Date must be formatted like “9/8/1636” or “September 8, 1636”")


main()
