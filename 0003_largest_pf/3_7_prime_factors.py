# Project Euler #3: Largest Prime Factor

# What is the largest prime factor of the number 600851475143 ?
import math as m

class Primes:

    def __init__(self):
        self.arr = []
        self.counter = 1
        self.number = 2

        self.sum_count = 0
    
    def list_primes(self, term):
        num_prime = 0
        i = 1
        while True:
            i += 1
            for j in range(2, int(m.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                num_prime += 1
                if num_prime >= term:
                    return i

    def prime_store(self, prime):
        self.arr.append(prime)

        return ""

    def prime_factors(self, number):
        for term in range(2, number):
            while number % term == 0:
                print(term)
                number = number / term
                self.prime_store(term)

                if number == 1:
                    return ""
        if len(self.arr) == 0:
            print(number)
        return ""
    
    def print_out(self):
        print("Enter a number:")
        while True:
            try:
                x = int(input())
            except:
                print("Invalid, please try again")
                continue
            else:
                break

        print("The prime factors of are:")
        print(self.prime_factors(x))

        print("The largest prime factor is: ")
        if len(self.arr) == 0:
            print(x)
        else:
            print(self.arr[len(self.arr) -1])

    def sum_of_primes(self, max_num):
        pass



#test1 = PrimeFactors()
#test1.print_out()

test2 = Primes()
print(test2.list_primes(10001))
test2.print_out()
