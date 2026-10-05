import re
import sys


def main():
	html = input("What's the HTML? ").strip()
	link = parse(html)
	if not link:
		sys.exit("Invalid HTML")
	print(f"There are the link: {link}")


def parse(html):
	match = re.search(r"^<iframe.*src=\"(?:https?://)?(?:www\.)?youtube.com/embed/(?P<url>.*?)\".*></iframe>$", html)
	if not match:
		return
	code = match.group("url")
	return f"https://youtu.be/{code}"


if __name__ == "__main__":
	main()
