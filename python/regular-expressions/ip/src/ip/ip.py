import re


def main():
	ip_address = input("What's the IPv4 addres? ").strip()
	if validate(ip_address):
		print("Valid")
	else:
		print("Invalid")


def validate(ip_address):
	matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip_address)
	if not matches:
		return False
	for match in matches.groups():
		if 0 > int(match) or int(match) > 255:
			return False
	return True


if __name__ == "__main__":
	main()
