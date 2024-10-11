/*
x_n: int = lambda n: ((1248 ** n) % 32323) - 16161
y_n: int = lambda n: ((8421 ** n) % 30103) - 15051

if __name__ == "__main__":
    x_8: list = [x_n(i) for i in range(1, 9)]
    y_8: list = [y_n(i) for i in range(1, 9)]
    P_8: object = zip(x_8, y_8)
    
    print("P_8 = {}".format(list(P_8)))
*/

#include <stdio.h>

int mod_exp(int base, int exp, int mod);

/*
 * run using these commands:
 *-$ gcc get_vertices.c -o get_vertices
 *-$ ./get_vertices > vertices.txt
*/
int main(int argc, char* argv[])
{
	for(int i = 1; i <= 2000000; i++)
	{
		int x_n = mod_exp(1248, i, 32323) - 16161;
		int y_n = mod_exp(8421, i, 30103) - 15051;
		//printf("i: %d, x_n: %d, y_n: %d\n", i, x_n, y_n); // for visualizing
		printf("%d, %d\n", x_n, y_n); // for saving to file
	}
	return 0;
}

/*
 * Modular exponentiation algorithm
 * -> (base^exp) % mod
 *
 * TC: O(log exp)
 * SC: O(1)
*/
int mod_exp(int base, int exp, int mod)
{
	int res = 1;
	base = base % mod;
	while(exp > 0)
	{
		// If exp is odd, multiply base with result
		if(exp % 2 == 1)
		{
			res = (res * base) % mod;
		}
		exp = exp >> 1; // Divide exp by 2
		base = (base * base) % mod; // Square the base
	}
	return res;
}

/* END FILE */