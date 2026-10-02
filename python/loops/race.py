"""
——— Source ———
From the shorts
——— Purpose ———
Example of list methods
"""


def main():
	race = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Bowser"]
	race.extend(["Toad", "Donkey Kong Jr."])
	race.remove("Bowser")
	race.insert(0, "Bowser")
	race.reverse()
	print(race)


main()
