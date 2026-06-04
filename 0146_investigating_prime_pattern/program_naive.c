// PE 0146: INVESTIGATING A PRIME PATTERN
// - JAMES DELEON

#include <stdio.h>
#include <stdbool.h>

bool is_prime(unsigned long long n)
{
	if(n < 2)
	{
		return false;
	}
	if(n == 2)
	{
		return true;
	}
	if(n % 2 == 0)
	{
		return false;
	}
	// Only test odd divisors up to sqrt(n)
	unsigned long long div = 3;
	while(div * div <= n)
	{
		if(n % div == 0)
		{
			return false;
		}
		div += 2;
	}
	return true;
}

int main(int argc, char* argv[])
{
	unsigned long long num_sum = 0;
	for(unsigned long long i = 40000000; i < 150000000; i += 2)
	{
		if(i % 1000000 == 0)		printf("Checkpoint: %lld\n", i);
		if(i % 3 == 0)				continue;
		if(!is_prime((i * i) + 27)) continue;
		if(!is_prime((i * i) + 13)) continue;
		if(!is_prime((i * i) + 9))  continue;
		if(!is_prime((i * i) + 7))  continue;
		if(!is_prime((i * i) + 3))  continue;
		if(!is_prime((i * i) + 1))  continue;

		printf("int: %lld\n", i);
		num_sum += i;
	}
	printf("sum: %lld\n", num_sum);
	return 0;
}
/* END FILE */