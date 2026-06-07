// GROSS/ZEITMAN ITERATIVE ALGORITHM
// - JAMES DELEON

#include <stdio.h>
#include <stdbool.h>

typedef long long lld;

#define M 4
#define N 2

/*
def solve_ack(m: int, n: int) -> int:
    '''
    #- Grossman/Zeitman iterative algorithm

    # for computing A(m, n) iteratively,
    # - requires O(m) space
    # - requires O(m * A(m, n)) time
    '''
    next_arr: list = [0 for i in range(0, m + 1)]
    goal_arr: list = [1 for i in range(0, m + 1)]
    
    goal_arr[-1] = -1
    while next_arr[m] != n + 1:
        value: int = next_arr[0] + 1
        transfer: bool = True
        curr_m: int = 0
        while transfer:
            if next_arr[curr_m] == goal_arr[curr_m]:
                goal_arr[curr_m] = value
            else:
                transfer = False
            next_arr[curr_m] += 1
            curr_m += 1
            #print(goal_arr)
    return value

if __name__ == "__main__":
    m: int = 5
    n: int = 1 
    print("A({0}, {1}) = {2}".format(m, n, solve_ack(m, n)))
*/

void print_arr(lld* arr, int arr_size)
{
	printf("[ ");
	for(int i = 0; i < arr_size; i++)
	{
		printf("%lld ", arr[i]);
	}
	printf("]\n");
}

lld solve_ack(int m, int n)
{
	lld next_arr[m + 1];
	lld goal_arr[m + 1];
	for(int i = 0; i < m + 1; i++)
	{
		next_arr[i] = 0;
		goal_arr[i] = 1;
	}
	goal_arr[m] = -1;

	lld value, curr_m;
	bool transfer;
	do
	{
		value = next_arr[0] + 1;
		curr_m = 0;
		transfer = true;
		while(transfer)
		{
			if(next_arr[curr_m] == goal_arr[curr_m])
			{
				goal_arr[curr_m] = value;
			}
			else
			{
				transfer = false;
			}
			next_arr[curr_m] += 1;
			curr_m += 1;
		}
		// print_arr(goal_arr, m + 1);
	} while(next_arr[m] != n + 1);
	return value;
}

int main(int argc, char* argv[])
{
	lld ack = solve_ack(M, N);
	printf("A(%d, %d) = %lld\n", M, N, ack);
	return 0;
}

/* END FILE */