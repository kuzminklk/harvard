import re
import sys


def main():
	html = input("What's the HTML? ").strip()
	link = parse(html)
	if not link:
		sys.exit("Invalid HTML")
	print(f"There are the link: {link}")


def parse(html):
	"""
	Parse HTML “<iframe>” for YouTube link

	Returns:
		Short link like “https://youtu.be/f3j9yjm3”
	"""
	match = re.search(r"^<iframe.*src=\"(?:https?://)?(?:www\.)?youtube.com/embed/(?P<url>.*?)\".*></iframe>$", html)
	if not match:
		return
	code = match.group("url")
	return f"https://youtu.be/{code}"


if __name__ == "__main__":
	main()
