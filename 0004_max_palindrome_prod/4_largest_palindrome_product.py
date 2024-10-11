# Project Euler #4: Largest Palindrome Product
import profile_function as p

class PalindromeProduct:

	def __init__(self, digit_num1, digit_num2):
		self.dig1 = digit_num1
		self.dig2 = digit_num2
		
		self.max_prod = 0
		self.prod_list = []

		self.range1_min = 10 ** self.dig1
		self.range1_max = 10 ** (self.dig1 + 1)
		self.range2_min = 10 ** self.dig2
		self.range2_max = 10 ** (self.dig2 + 1)

	def all_pal_products(self):
		for i in range(self.range1_min, self.range1_max):
			for j in range(self.range2_min, self.range2_max):
				product = i * j
				if str(product) == str(product)[::-1]:
					self.prod_list.append(product)
		return self.prod_list

	@p.profile
	def max_pal_product(self):
		gather = self.all_pal_products()
		for i in range(len(gather)):
			if gather[i] > self.max_prod:
				self.max_prod = gather[i]
		return self.max_prod

test1 = PalindromeProduct(1, 3)
print(test1.max_pal_product())
# the largest palindromic number of the product of two
#  three-digit integers is:

# 906609