"""
——— Source ———
From the problem set
——— Behavior ———
Asks for the file extension, then show appropriate MIME type
"""


def main():
	extension = input("What's file name (with extension)? ")
	extension = extension.strip().lower()
	print(f"MIME type is {extension_to_mime_type(extension)}")


def extension_to_mime_type(extension):
	if extension.endswith(".gif"):
		return "image/gif"
	elif extension.endswith((".jpg", "jpeg")):
		return "image/jpeg"
	elif extension.endswith(".png"):
		return "image/png"
	elif extension.endswith(".pdf"):
		return "application/pdf"
	elif extension.endswith(".zip"):
		return "application/zip"
	else:
		return "application/octet-stream"


main()
