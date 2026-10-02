"""
——— Source ———
From the problem set
——— Description ———
Counts lines of code for the Python file
"""

import sys


def main():
	count = 0
	file = sys.argv[1].strip()
	try:
		with open(file) as file:
			count = count_lines(file)
	except FileNotFoundError:
		sys.exit(f"Usage: {sys.argv[0]} file")
	print(f"There are {count} lines of code!")


def count_lines(file):
	count = 0
	for line in file:
		if line.lstrip().startswith("#") or line.strip() == "":
			continue
		else:
			count += 1
	return count


main()
