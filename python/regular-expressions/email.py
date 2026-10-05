"""
——— Source ———
From the lecure
——— Description ———
Validates email
"""

import re


def main():
	email = input("What's an email? ")

	if re.search(r"^\w+@(\w+\.)*\w+\.(edu|com|gov)$", email, re.IGNORECASE):
		print("Valid")
	else:
		print("Invalid")


main()
