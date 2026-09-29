"""
——— Source ———
From the problem set
——— Description ———
Notes grocery list, finally shows as sorted
"""


def main():
	grocery_list = []
	while True:
		try:
			item = input("Item: ").strip().title()
			grocery_list.append(item)
		except EOFError:
			show_groceries(grocery_list)
			return


def show_groceries(grocery_list):
	print("\n\nFinal list is:")
	grocery_list = sorted(grocery_list)
	grocery_dictionary = {item: grocery_list.count(item) for item in grocery_list}
	for item in grocery_dictionary:
		print(f"{grocery_dictionary[item]} {item}")


main()
