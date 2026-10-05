"""
——— Source ———
From the lecure
——— Description ———
Grab username
"""

import re


def main():
	url = input("What's the URL? ").strip()

	if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
		print(f"Hello, {matches.group(1)}!")


main()
