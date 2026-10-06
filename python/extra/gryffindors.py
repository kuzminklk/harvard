"""
——— Source ———
From the lecture
——— Purpose ———
Example of list “filter” and lambda functions
"""

students = [
	{"name": "Hermione", "house": "Gryffindor"},
	{"name": "Harry", "house": "Gryffindor"},
	{"name": "Ron", "house": "Gryffindor"},
	{"name": "Draco", "house": "Slytherin"},
]

gryffindors = filter(lambda student: student["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
	print(gryffindor["name"])
