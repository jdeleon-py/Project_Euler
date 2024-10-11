# Project Euler #1: Multiples of 3 and 5

# Find the sum of all the multiples of either 3 or 5 below 1000.

class MultiplesSum:

	def __init__(self, sum_range, num1, num2):
		self.range = sum_range
		self.num1 = num1
		self.num2 = num2
		self.counter = 0

	def is_multiple(self, x, y):
		if x % y == 0:
			return True
		return False

	def sum(self):
		for multiple in range(self.range):
			if self.is_multiple(multiple, self.num1):
				self.counter += multiple
			elif self.is_multiple(multiple, self.num2):
				self.counter += multiple
			else:
				self.counter += 0
		return self.counter

test1 = MultiplesSum(1000, 3, 5)
print(test1.sum())
# The sum of all multiples of 3 and 5 below 1000 is 233168.

test2 = MultiplesSum(500, 2, 13)
print(test2.sum())

# Classes are a better way of implementing software than hardcoding, as seen below
'''
sum_of_multiples = 0
for number in range(1,1000):
    if number % 3 == 0:
        sum_of_multiples += number
    elif number % 5 == 0:
        sum_of_multiples += number
    else:
        continue
print(sum_of_multiples)

'''