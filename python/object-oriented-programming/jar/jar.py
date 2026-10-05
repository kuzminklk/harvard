class Jar:
	def __init__(self, capacity=12):
		self.capacity = capacity
		self.size = 0

	def __str__(self):
		return "🍪" * self.size

	def deposit(self, amount):
		if amount + self.size > self.capacity:
			raise ValueError("Final amount greater than capacity")
		self.size += amount

	def withdraw(self, amount):
		self.size -= amount

	@property
	def capacity(self):
		return self._capacity

	@capacity.setter
	def capacity(self, value):
		if int(value) < 0:
			raise ValueError("Capacity can't be less than zero")
		self._capacity = value

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, value):
		if int(value) < 0:
			raise ValueError("Size can't be less than zero")
		self._size = value
