"""
——— Source ———
From the lecture
——— Purpose ———
Example of dictionary comprehension
"""

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
