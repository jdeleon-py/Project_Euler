def collatz_sequence(number) -> int:
	iterations = 0
	while True:
		if(number == 1):
			# print("Iterations: " + str(iterations))
			return iterations
		elif(number % 2 > 0):
			number = (3 * number) + 1
			# print(number)  
		else:
			number = (number // 2)
			# print(number)
		iterations = iterations + 1

if __name__ == "__main__":
	largest_seq: int = 1
	largest_num: int = 1

	for i in range(1, 1000000):
		curr: int = collatz_sequence(i)
		if curr > largest_seq:
			largest_seq = curr
			largest_num = i
	print("Largest num: {}".format(largest_num))
	print("Largest seq: {}".format(largest_seq))
