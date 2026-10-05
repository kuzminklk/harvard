import re
import sys


def main():
	text = input("What's the text? ").strip()
	print(f"There are {count(text)} “um”")


def count(text):
	pattern = r"\bum\b"
	matches = re.findall(pattern, text, flags=re.IGNORECASE)
	if not matches:
		return 0
	else:
		return len(matches)


if __name__ == "__main__":
	main()
