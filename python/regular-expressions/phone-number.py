"""
——— Source ———
From the shorts
——— Description ———
Validates phone number and grabs country code
"""

import re


locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua	"}


def main():
	pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
	number = input("What's the number? ")

	if match := re.search(pattern, number, re.IGNORECASE):
		print("Valid")
		country_code = match.group("country_code")
		print(f"Location is {locations[country_code]}")
	else:
		print("Invalid")


main()
