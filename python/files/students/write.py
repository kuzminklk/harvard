import csv

name = input("What's your name? ").strip().lower().title()
home = input("Where are you frome? ").strip().lower().title()

with open("students.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames=["name", "home"])
	writer.writerow({"name": name, "home": home})
