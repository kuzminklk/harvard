import sys
import csv
from tabulate import tabulate


def main():
	file_name = sys.argv[1].strip()
	if not file_name.lower().endswith(".csv"):
		sys.exit(f"Usage: {sys.argv[0]} file.csv")
	try:
		with open(file_name) as file:
			reader = csv.reader(file)
			print(tabulate(reader, tablefmt="grid"))
	except FileNotFoundError:
		sys.exit(f"Usage: {sys.argv[0]} file.csv")


if __name__ == "__main__":
	main()
