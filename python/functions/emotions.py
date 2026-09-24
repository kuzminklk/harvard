"""
From the shorts.
Example of side effects of function running.
Like changing state or printing a message…
"""

# Global variable
emoticon = "v.v"


def main():
	# Access to change global variable
	global emoticon
	say("Is anyone there?")
	emoticon = ":D"
	say("Oh, hi!")


def say(phrase):
	print(f"{phrase} {emoticon}")


main()
