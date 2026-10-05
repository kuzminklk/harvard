import json
import requests
import sys


def main():
	if len(sys.argv) < 2:
		sys.exit(f"Usage: {sys.argv[0]} artist")

	try:
		response = requests.get("https://itunes.apple.com/search", {"entity": "song", "limit": 10, "term": sys.argv[1]})
		object = response.json()
	except requests.HTTPError:
		print("Can't connect!")

	for result in object["results"]:
		print(result["trackName"])


if __name__ == "__main__":
	main()
