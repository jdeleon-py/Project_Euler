// PROJECT EULER 145 MAIN PROGRAM
// - James deLeon (translated to C)

#include <stdio.h>
#include <stdlib.h>

#define LIMIT 1000000000

int reverse(int n);
int is_reversible(int n);

int main(int argc, char* argv[])
{
    int acc = 0;
    for (int i = 1; i < LIMIT; i++) {
        if(i % 10 != 0 && is_reversible(i))
        {
            acc++;
        }
        if(i % 50000 == 0)
        {
            printf("%d: %d\n", i, acc);
        }
    }
    printf("reversible count: %d\n", acc);
    return 0;
}

int reverse(int n)
{
    int rev = 0;
    while(n > 0)
    {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev;
}

int is_reversible(int n)
{
    int sum = n + reverse(n);
    while (sum > 0)
    {
        int digit = sum % 10;
        if(digit % 2 == 0)
        {
            return 0;  // Even digit found
        }
        sum /= 10;
    }
    return 1;  // All digits are odd
}
