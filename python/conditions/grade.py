"""
——— Source ———
From the lecture
——— Behavior ———
Takes the score and calculates grade from it, then prints
——— Purpose ———
Example of conditional operators
"""


def main():
	score = int(input("What's is score? "))

	if score >= 90:
		print("Grade: A")
	elif score >= 80:
		print("Grade: B")
	elif score >= 70:
		print("Grade: C")
	elif score >= 60:
		print("Grade: D")
	else:
		print("Grade: F")


main()
