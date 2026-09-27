"""
——— Source ———
From the problem set
——— Behavior ———
Asks for the greeting, then decides which message to show
"""


def main():
	greeting = input("What's greeting? ")
	greeting = greeting.strip().lower()
	if greeting.startswith("hello"):
		print("You get $0")
	elif greeting.startswith("h"):
		print("You get $20")
	else:
		print("You get $100")


main()
