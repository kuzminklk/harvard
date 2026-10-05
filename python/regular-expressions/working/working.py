import re
import sys


def main():
	time = input("What's the time? ").strip()
	try:
		converted_time = convert(time)
	except ValueError:
		print("Invalid input")
	print(converted_time)


def convert(time):
	pattern = r"^(?P<beginning_hours>[0-9]{1,2}):?(?P<beginning_minutes>[0-9]{2})? (?P<beginning_meridiem>AM|PM) to (?P<ending_hours>[0-9]{1,2}):?(?P<ending_minutes>[0-9]{2})? (?P<ending_meridiem>AM|PM)$"

	matches = re.search(
		pattern,
		time,
	)

	# — Input validation —
	if (
		not matches
		or (len(matches.groups()) < 6)
		or (int(matches.group("beginning_hours")) > 12 or int(matches.group("ending_hours")) > 12)
	):
		raise ValueError("Invalid input")

	if not matches.group("beginning_minutes"):
		beginning_minutes = 0
	else:
		beginning_minutes = int(matches.group("beginning_minutes"))

	if not matches.group("ending_minutes"):
		ending_minutes = 0
	else:
		ending_minutes = int(matches.group("ending_minutes"))

	if beginning_minutes >= 60 or ending_minutes >= 60:
		raise ValueError("Invalid input")

	# — Meridiem transition logic —
	if matches.group("beginning_meridiem") == "AM":
		coverted_beginning_hours = int(matches.group("beginning_hours"))
	elif matches.group("beginning_meridiem") == "PM":
		coverted_beginning_hours = int(matches.group("beginning_hours")) + 12

	if matches.group("ending_meridiem") == "AM":
		coverted_ending_hours = int(matches.group("ending_hours"))
	elif matches.group("ending_meridiem") == "PM":
		coverted_ending_hours = int(matches.group("ending_hours")) + 12

	return f"{coverted_beginning_hours:02}:{beginning_minutes:02} to {coverted_ending_hours:02}:{ending_minutes:02}"


if __name__ == "__main__":
	main()
