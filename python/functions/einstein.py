"""
From the problem set.
Turn mass to energy by (E=mc^2) formula. Takes user input as mass (in kilograms) and print the energy (in Joules)
"""

# Approximately
SPEED_OF_LIGHT = 300000000


def main():
	mass = int(input("Write an mass: "))
	energy = mass * (300000000**2)
	print(f"The enegry is {energy} Joules!")


main()
