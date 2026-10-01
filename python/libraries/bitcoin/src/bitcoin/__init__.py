import requests
import sys
import os
from dotenv import load_dotenv


def main():
	load_dotenv()
	try:
		response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", {"apiKey": os.getenv("COINCAP_API_KEY")})
		object = response.json()
	except (requests.HTTPError, requests.RequestException):
		print("Can't connect!")

	price = object["data"]["priceUsd"]
	price = float(price)

	if len(sys.argv) == 1:
		print(price)
	else:
		try:
			value = float(sys.argv[1])
			print(value * price)
		except ValueError:
			sys.exit(f"Usage: {sys.argv[0]} [value]")


def take_a_positive_number(message):
	while True:
		number = input(message).strip()

		try:
			number = int(number)
			if number < 0:
				print("Write a positive number!")
			else:
				return number
		except ValueError:
			print("Write a number!")


if __name__ == "__main__":
	main()
