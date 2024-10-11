# Pythagorean Theorem: a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

class PythgoreanAnalysis:

	def __init__(self):
		self.a = []
		self.b = []
		self.c = []

	def py_triplet(self, max_num):
		for x in range (1, max_num):
			for y in range (1, max_num):
				for z in range(1, max_num):
					if (x ** 2) == (y ** 2) + (z ** 2):
						if(x + y + z == max_num):
							return (x, y, z)

test1 = PythgoreanAnalysis()
print(test1.py_triplet(1000))