import sys
from PIL import Image


def main():
	images = []

	for arg in sys.argv[1:]:
		with Image.open(arg) as image:
			images.append(image)

	images[0].save("cat-full.gif", save_all=True, append_images=[images[1]], duration=200, loop=0)


if __name__ == "__main__":
	main()
