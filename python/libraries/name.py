"""
——— Source ———
From the lecture
——— Description ———
Shuffle cards
"""

import sys


def main():
	if len(sys.argv) < 2:
		sys.exit(f"usage: {sys.argv[0]} name [names …]")
	for name in sys.argv[1:]:
		print(f"Hello! My name is {name}")


main()
