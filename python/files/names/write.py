import sys

with open("names.txt", "a") as file:
	while True:
		try:
			name = input("What's a name? ").strip().lower().title()
			file.write(f"{name}\n")
		except EOFError:
			print("\nProgram closed")
			sys.exit()
