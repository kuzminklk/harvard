"""
——— Source ———
From the lecture
——— Description ———
Formats name
"""

import re


def main():
	name = input("What's your name? ")

	if matches := re.search(r"^(.+), *(.+)$", name):
		name = matches.group(2) + " " + matches.group(1)
	print(f"Hello, {name}!")


main()
