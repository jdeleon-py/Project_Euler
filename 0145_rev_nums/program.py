# PROJECT EULER 145 MAIN PROGRAM
# - James deLeon

get_rev: int = lambda n: int("".join([i for i in str(n)][::-1]))

def is_reversible(n: int) -> bool:
    rev_num: int = n + get_rev(n)
    rev_arr: list = [int(i) for i in str(rev_num)]
    all_odd: bool = True
    for digit in rev_arr:
        if digit % 2 == 0:
            return False
    return True

if __name__ == "__main__":
    acc: int = 0
    for i in range(1, 1000000000):
        #- add extra condition for numbers that end in zero, since no leading 
        # zeroes are allowed for its reversed counterpart
        if is_reversible(i) and (i % 10 != 0):
            acc += 1
        if i % 50000 == 0: print("{0}: {1}".format(i, acc))
    print("reversible count: {}".format(acc))
