"""
——— Source ———
From the problem set
——— Description ———
Say adieu (goodbye in French) for given names
"""


def main():
	names = []
	while True:
		try:
			name = input("What's the name? ")
			names.append(name)
		except EOFError:
			break
	print_names(names)


def print_names(names):
	if len(names) == 1:
		print(f"Adieu, adieu, to {names[0]}")
	elif len(names) == 2:
		print(f"Adieu, adieu, to {names[0]} and {names[1]}")
	else:
		names_with_comma = ", ".join(names[:-1])
		print(f"Adieu, adieu, to {names_with_comma} and {names[-1]}")


if __name__ == "__main__":
	main()
