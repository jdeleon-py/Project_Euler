# PE 0035: CIRCULAR PRIMES
# - JAMES DELEON

import random

K: int = 3           #- parameter for Fermat's Primality Test
LIMIT: int = 1000000 #- how many primes are we testing for circularity?

# for generating a range of prime numbers less than or equal to _num
def generate_primes(num: int) -> list:
    '''
    - generates a list of prime numbers less than
    or equal to _num
    '''
    primes: list = []
    for n in range(2, num + 1):
        is_prime: bool = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(n)
    return primes

def rotate(arr: list) -> list:
    temp: int = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = temp
    return arr

# Iterative Function to calculate 
# (a^n) % p in O(logy) 
def power(a: int, n: int, p: int): 
    res: int = 1                     # Initialize result
    a = a % p                        # Update 'a' if 'a' >= p 
    while n > 0:
        if n % 2 == 1:               # if n is odd, multiply result by 'a'
            res = (res * a) % p
            n -= 1
        else:                        # n must be even now
            a = (a ** 2) % p 
            n = n // 2
    return res % p
    
# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def is_prime(n: int, k: int):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(0, k): # Try k times 
            # Pick a random number 
            # in [2..n-2]      
            a = random.randint(2, n - 2)
            
            # Fermat's little theorem 
            if power(a, n - 1, n) != 1:
                return False            
    return True

if __name__ == "__main__":
    count: int = 0      # count of circular primes
    circ_arr: list = [] # array of circular primes

    prime_arr: list = generate_primes(LIMIT)
    for prime in prime_arr:
        prime_arr: list = [int(ch) for ch in str(prime)]
        count += 1
        for _ in range(0, len(prime_arr) - 1):
            # rotate the prime digit array n - 1 times, since
            # we know already that n = 0 case is prime
            prime_arr = rotate(prime_arr)
            if not is_prime(int("".join([str(i) for i in prime_arr])), K):
                # remove this non circular prime from the count and try the next one
                count -= 1
                break
        else:
            circ_arr.append(prime)
    print("Number of circular primes: {}".format(count))
    print("{}".format(circ_arr))

# END FILE #