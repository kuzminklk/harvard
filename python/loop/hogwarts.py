"""
——— Source ———
From the lecture
——— Behavior ———
Prints Hogwarts students, their houses and patronuses
——— Purpose ———
Example of dictionary and for loop
"""

students = [
	{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
	{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
	{"name": "Eon", "house": "Gryffindor", "patronus": "Jask Russel terrier"},
	{"name": "Draco", "house": "Slytherin", "patronus": None},
]


def main():
	for student in students:
		print(student["name"], student["house"], student["patronus"], sep=", ")


main()
