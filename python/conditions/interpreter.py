"""
——— Source ———
From the problem set
——— Behavior ———
Asks for two variable and one operator, then do mathematic
"""


def main():
	expression = input("What's expression? ")
	expression = expression.strip().lower()
	x, operator, z = expression.split(" ")
	x = float(x)
	z = float(z)
	result = math(x, operator, z)
	print(f"Result is {result:.2f}")


def math(x, operator, z):
	match operator:
		case "+":
			return x + z
		case "-":
			return x - z
		case "*":
			return x * z
		case "/":
			if z == 0:
				return
			else:
				return x / z


main()
