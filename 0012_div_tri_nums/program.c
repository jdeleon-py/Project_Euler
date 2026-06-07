// PROJECT EULER 0012: HIGHLY DIVISIBLE TRIANGULAR NUMBERS
// - JAMES DELEON

#include <stdio.h>
#include <stdbool.h>

/*
# This function computes the factor of the argument passed
def get_factors(n: int) -> int:
    factors: int = 0
    # factors: list = []
    for i in range(1, n + 1):
        if n % i == 0:
            #factors.append(i)
            factors += 1
    return factors

if __name__ == "__main__":
    adder: int = 2
    num: int = 1
    divs: int = 500
    while True:
        factors: list = get_factors(num)
        if factors > divs:
            print("First with over {0} factors: {1}".format(divs, num))
            print("Number of factors: {}".format(factors))
            #print("Factors: {}".format(factors))
            break
        num += adder
        adder += 1
*/

#define DIVS 500

int count_factors(int num)
{
	int count = 0;
	for(int i = 0; i <= num; i++)
	{
		if(num % i == 0)
		{
			count += 1;
		}
	}
	return count;
}

int main(int argc, char* argv[])
{
	int adder, num, count;

	num = 1; adder = 2;
	while(true)
	{
		count = count_factors(num);
		if(count > DIVS)
		{
			printf("First number with over %d factors: %d\n", DIVS, num);
			printf("Number of factors: %d\n", count);
			break;
		}
		num += adder;
		adder += 1;
	}
	return 0;
}

/* END FILE */