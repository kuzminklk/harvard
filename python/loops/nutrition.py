"""
——— Source ———
From the problem set
——— Description ———
Show calories per fruit
"""

calories_per_fruit = {
	"apple": 130,
	"avocado": 50,
	"banana": 110,
	"cantaloupe": 50,
	"grapefruit": 60,
	"grapes": 90,
}


def main():
	fruit = input("What's the fruit? ").strip().lower()
	if fruit in calories_per_fruit:
		print(f"Calories: {calories_per_fruit[fruit]}")


main()
