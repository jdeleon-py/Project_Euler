'''
- length of squared number is 19 digits whose MSB is 1
so 2nd MSB must be between 0-9

- let y_min = 1,000,000,000
- let y_max = 1,500,000,000
- y_min ** 2 => 1e19
- y_max ** 2 => 2e19 (out of bounds for desired result)

- we have reduced the problem by needing to check
500,000,000 numbers: 1B <= n <= 1.5B
'''

BASE_NUM = 1000000000

START_INC = 1010101010 # all empty digits in desired result is 0
END_INC = 1389026620   # all empty digits in desired result is 9

def checker(arr: list) -> bool:
    return ((arr[0] == 1) and (arr[2] == 2) and (arr[4] == 3) and 
            (arr[6] == 4) and (arr[8] == 5) and (arr[10] == 6) and
            (arr[12] == 7) and (arr[14] == 8) and (arr[16] == 9) and (arr[18] == 0))

if __name__ == "__main__":
    for i in range(END_INC, START_INC, -10):
        x_arr: list = [int(j) for j in str((i) ** 2)]
        ch: bool = checker(x_arr)
        print("sq_digit_arr = {0}; match? {1}".format(x_arr, ch))
        if ch == True:
            break
