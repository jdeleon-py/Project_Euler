'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + 3^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + 3 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is,
3025−385=2640

Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.
'''
import profile_function as p

class SumSquareDiff:

	def __init__(self, min_num, max_num):
		self.min = min_num
		self.max = max_num
		self.count_sum = 0
		self.count_square = 0

	def sum_of_squares(self):
		for i in range(self.min, self.max + 1):
			self.count_sum += i ** 2
		return self.count_sum

	def square_of_sums(self):
		for i in range(self.min, self.max + 1):
			self.count_square += i
		return self.count_square ** 2

	@p.profile
	def difference(self):
		return self.square_of_sums() - self.sum_of_squares()

test1 = SumSquareDiff(1, 10)
print(test1.difference())

test2 = SumSquareDiff(1, 100)
print(test2.difference())