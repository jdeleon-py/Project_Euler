// PE 0146: INVESTIGATING A PRIME PATTERN (FERMAT'S PRIMALITY TEST)
// - JAMES DELEON

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

typedef unsigned long long ull;

// Safe modular multiplication: (a * b) % mod
// Uses GCC/Clang extension __uint128_t
ull mul_mod(ull a, ull b, ull mod)
{
	return (__uint128_t)a * b % mod;
}

// Computes (a^n) % p in O(log n)
ull power_mod(ull a, ull n, ull p)
{
	ull res = 1;
	a = a % p;
	while(n > 0)
	{
		if(n % 2 == 1)
		{
			res = mul_mod(res, a, p);
			n -= 1;
		} 
        else
        {
			a = mul_mod(a, a, p);
			n /= 2;
		}
	}
	return res % p;
}

// Random unsigned long long in range [low, high]
ull rand_ull_range(ull low, ull high)
{
	ull range = high - low + 1;
	ull r = 0;
	r ^= (ull)rand();
	r ^= (ull)rand() << 15;
	r ^= (ull)rand() << 30;
	r ^= (ull)rand() << 45;
	r ^= (ull)rand() << 60;
	return low + (r % range);
}

// Fermat primality test
bool isPrime(ull n, int k)
{
	if (n == 1 || n == 4)
	{
		return false;
	} 
	else if(n == 2 || n == 3)
	{
		return true;
	} 
	else 
	{
		for(int i = 0; i < k; i++) 
		{
			// Pick random a in [2, n - 2]
			ull a = rand_ull_range(2, n - 2);

			// Fermat's little theorem
			if (power_mod(a, n - 1, n) != 1) 
			{
				return false;
			}
		}
	}
	return true;
}

int main(int argc, char* argv[]) 
{
	ull num_sum = 0;
	int k = 3;
	srand((unsigned int)time(NULL));
	for(ull i = 4; i < 150000000ULL; i += 2) 
	{
		if(i % 1000000ULL == 0)
		{
			printf("Checkpoint: %llu\n", i);
		}
		if(i % 3ULL == 0)
		{
			continue;
		}
		ull square = i * i;
		// these must be prime to pass through
		if(!isPrime(square + 27ULL, k)) continue;
		if(!isPrime(square + 13ULL, k)) continue;
		if(!isPrime(square + 9ULL,  k)) continue;
		if(!isPrime(square + 7ULL,  k)) continue;
		if(!isPrime(square + 3ULL,  k)) continue;
		if(!isPrime(square + 1ULL,  k)) continue;

		// account for every odd offset between the targets
		// since we are looking for "consecutive" primes
		// these must be composite to pass through
		if(isPrime(square + 25ULL, k)) continue;
		if(isPrime(square + 23ULL, k)) continue;
		if(isPrime(square + 21ULL, k)) continue;
		if(isPrime(square + 19ULL, k)) continue;
		if(isPrime(square + 17ULL, k)) continue;
		if(isPrime(square + 15ULL, k)) continue;
		if(isPrime(square + 11ULL, k)) continue;
		if(isPrime(square + 5ULL, k))  continue;
		printf("int: %llu\n", i);
		num_sum += i;
	}
	printf("sum: %llu\n", num_sum);
	return 0;
}