// MODULAR EXPONENTIATION ALGORITHM
// - JAMES DELEON

#include <stdio.h>
#include <stdint.h>

uint64_t mod_exp(uint64_t base, uint64_t exp, uint64_t mod)
{
	uint64_t result = 1;
	base = base % mod;
	while(exp > 0)
	{
		if(exp % 2 == 1)
		{
			result = (result * base) % mod;
		}
		base = (base * base) % mod;
		exp = exp / 2;
	}
	return result;
}

int main(int argc, char* argv[])
{
	uint64_t base = 2;
	uint64_t exp = 65536;
	uint64_t mod = 1475789056;
	uint64_t answer = mod_exp(base, exp, mod);

	printf("%llu^%llu mod %llu = %llu\n", base, exp, mod, answer);
	return 0;
}

/* END FILE */