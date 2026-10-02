import sys
import csv


def main():

	if not sys.argv[1] or not sys.argv[1]:
		sys.exit(f"Usage: {sys.argv[0]} input_file.csv output_file.csv")

	input_file_name = sys.argv[1].strip().lower()
	output_file_name = sys.argv[2].strip().lower()

	try:
		with open(input_file_name) as input_file, open(output_file_name, "w") as output_file:
			reader = csv.DictReader(input_file)
			writer = csv.DictWriter(output_file, fieldnames=["first_name", "last_name", "house"])
			writer.writeheader()
			for person in reader:
				first_name, last_name = person["name"].split(", ")
				new_person = {"first_name": first_name, "last_name": last_name, "house": person["house"]}
				writer.writerow(new_person)

	except FileNotFoundError:
		sys.exit(f"Usage: {sys.argv[0]} file")


main()
