# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that 
# is evenly divisible by all of the numbers from 1 to 20?
import profile_function as p

class SmallestMultiple:

	def __init__(self, min_num, max_num):
		self.min = min_num
		self.max = max_num
		self.num = 1

	def operation(self, num):
		for i in range(self.min, self.max + 1):
			if num % i != 0:
				return False
		return True

	@p.profile
	def smallest_mult(self):
		while True:
			if self.operation(self.num):
				print("Smallest multiple:")
				print(self.num)
				break
			else:
				if self.num == 1:
					self.num = self.num * self.max
					continue
				else:
					self.num += self.max # always a multiple of the maximum number (optimizes the program a bit)
					continue
		return ""

test1 = SmallestMultiple(1, 10)
print(test1.smallest_mult())

test2 = SmallestMultiple(1, 20)
print(test2.smallest_mult())

#The smallest positve number divisible by all numbers from 1 to 20 is 232792560.
