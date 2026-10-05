def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(string):
	return check_length(string) and check_start(string) and check_numbers(string) and check_marks(string)


def check_length(string):
	return 2 <= len(string) <= 6


def check_start(string):
	start = string[:2]
	for character in start:
		if character.isdecimal():
			return False
	return True


def check_numbers(string):
	check = False
	for character in string:
		if character.isdigit():
			if not check and character == "0":
				return False
			check = True
		else:
			if check:
				return False
	return True


def check_marks(string):
	return string.isalnum()


if __name__ == "__name__":
	main()
