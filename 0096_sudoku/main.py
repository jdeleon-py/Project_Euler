# PE_0096 MAIN PROGRAM
# - JAMES DELEON

from solver import Solver

FILENAME: str = "sudoku.txt"

if __name__ == "__main__":
    with open(FILENAME, "r") as file:
        data: list = file.read()
        data = data.split("\n")
        data = [i for i in data if "Grid" not in i] #-remove grid numbering
    file.close()
    #-create puzzles by splitting data into chunks of 9
    puzzles: list = [data[i: i + 9] for i in range(0, len(data) + 1, 9)][:-1]
    #-convert str in each puzzle into a list[9] of ints
    sudokus: list = [[[int(i) for i in line] for line in puzzle] for puzzle in puzzles]
    
    counter: int = 0 #-program counter for PE009 solution
    
    # feed each sudoku into solver api   
    for puzzle in sudokus:
        solver: object = Solver(puzzle, io_type = [True, False], verbose = False)
        solver.solve()
        print("{}".format(solver.solution))
        
        #-convert first 3 idxs on first row of each puzzle to an int and increment counter
        num: int = int(''.join(map(str, puzzle[0][0:3])))
        counter += num
        print("num: {0}, counter: {1}".format(num, counter))
    print("Done.")
