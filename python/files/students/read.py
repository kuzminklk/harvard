import csv

with open("students.csv") as file:
	reader = csv.DictReader(file)
	for row in sorted(reader, key=lambda student: student["name"]):
		print(f"{row['name']} is from {row['home']}")
