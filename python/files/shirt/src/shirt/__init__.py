import sys
import os
from pathlib import Path
from PIL import Image, ImageOps


def main():
	acceptable_extensions = [".jpg", ".jpeg", ".png"]
	usage_message = f"Usage: {sys.argv[0]} photo.jpg output_photo.jpg"

	if len(sys.argv) != 3:
		sys.exit("Invalid number of arguments\n" + usage_message)

	photo_file_name = sys.argv[1]
	new_photo_file_name = sys.argv[2]

	photo_extension = os.path.splitext(photo_file_name)[1].lower()
	new_photo_extension = os.path.splitext(new_photo_file_name)[1].lower()

	if (
		photo_extension not in acceptable_extensions
		or new_photo_extension not in acceptable_extensions
		or photo_extension != new_photo_extension
	):
		sys.exit("Extensions error\n" + usage_message)

	shirt_path = Path(__file__).resolve().parent / "shirt.png"

	try:
		with Image.open(shirt_path) as shirt, Image.open(photo_file_name) as photo:
			shirt_size = shirt.size
			resized_photo = ImageOps.fit(photo, shirt_size)
			resized_photo.paste(shirt, shirt)
			resized_photo.save(new_photo_file_name)
			print(f"Saved new photo as {new_photo_file_name}")

	except FileNotFoundError:
		sys.exit("File not found\n" + usage_message)


if __name__ == "__main__":
	main()
