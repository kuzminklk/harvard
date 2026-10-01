from pyfiglet import Figlet
import random
import sys


def main():
	figlet = Figlet()
	fonts = figlet.getFonts()
	figlet.setFont(font=random.choice(fonts))
	text = input("What's the text? ")

	if len(sys.argv) == 2:
		font = sys.argv[1]
		if font in fonts:
			figlet.setFont(font=font)
		else:
			sys.exit(f"Usage: {sys.argv[0]} [-f or --font] [font]")
	elif len(sys.argv) == 3:
		if sys.argv[1] in ["-f", "--font"]:
			font = sys.argv[2]
			figlet.setFont(font=font)
		else:
			sys.exit(f"Usage: {sys.argv[0]} [-f or --font] [font]")
	print(figlet.renderText(text))


if __name__ == "__main__":
	main()
