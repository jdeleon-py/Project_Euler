'''
- there is a mathematical solution regarding the indepedent probabilities
for each point in both X, Y distributions:
- https://robguzmantechblog.wordpress.com/2014/07/12/project-euler-205-dice-game/

- I would like to see if a solution can be gathered using a purely 
Monte Carlo based approach
'''

# this test only counts the number of wins of player 1 (n,k) = (9,4)

import random

N1: int = 9
K1: int = 4

N2: int = 6
K2: int = 6

SAMPLE_MAX: int = 10000000

if __name__ == "__main__":
    dice_arr1: list = [[k + 1 for k in range(0, K1)] for _ in range(0, N1)]
    dice_arr2: list = [[k + 1 for k in range(0, K2)] for _ in range(0, N2)]
    
    for trial in range(0, 50):
        win1_count: int = 0 #-number of wins accumulated by player 1
        for _ in range(0, SAMPLE_MAX):
            temp_sum1: int = 0
            #-player 1: guy with 9 4-sided dice
            for dice in dice_arr1:
                temp_sum1 += random.choice(dice)
            temp_sum2: int = 0
            #-player 1: guy with 6 6-sided dice
            for dice in dice_arr2:
                temp_sum2 += random.choice(dice)
            if temp_sum1 > temp_sum2:
                win1_count += 1
        print("Player 1 Win Probability - Trial {0}: {1}".format(trial, win1_count / SAMPLE_MAX))
