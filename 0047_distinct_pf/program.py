# PE0047 MAIN PROGRAM
# - pretty straightforward

N: int = 1000000                    # max of numbers to factor
LEN: int = 4                       # number of distinct pfs
    
def distinct_pf(num: int) -> list:
    '''
    - generates the list of DISTINCT prime factors of a 
    given positive integer num
    '''
    prime_factors: list = []
    for term in range(2, num):
        while num % term == 0:
            if num == 1:
                return
            num = num / term
            prime_factors.append(term)
    return list(set(prime_factors))

if __name__ == "__main__":
    consec: int = 0
    consec_max: int = 0
    
    limit: int = LEN
    # print all ints that have LEN distinct prime factors
    for i in range(0, N):
        pfs: list = distinct_pf(i)
        if len(pfs) == LEN:
            consec += 1
            print("i: {0}, pfs: {1}, consec: {2}, consec_max: {3}".format(i, pfs, consec, consec_max))
        else:
            consec = 0
        consec_max = max(consec_max, consec)
