"""
——— Source ———
From the shorts
——— Description ———
Validates hexadecimal color
"""

import re


def main():
	color = input("What's the color? ").strip()

	if matches := re.search(r"^#[a-f0-9]{6}$", color, re.IGNORECASE):
		print("Valid")
	else:
		print("Invalid")


main()
