import hexadoku
import backtracking
import time

###
 #  Records the time and success rate of the backtracking algorithm over n hexadoku 
 #  boards each starting with m clues (prefilled cells), given n and m as input
###

upper_bound = int(input("Upper clue bound (inclusive): "))
lower_bound = int(input("Lower clue bound (inclusive): "))
num_types = upper_bound - lower_bound
num_iterations = int(input("Iterations per board type: "))
print("")
real_start = time.time()
for num_clues in range (upper_bound, lower_bound-1, -1):
    num_solved = 0
    total_time = 0
    avg_time = 0

    for i in range (num_iterations):

        # initialize board
        completed_board = hexadoku.initialize_full_board()
        unfinished_board = hexadoku.initialize_partial_board(completed_board, num_clues)[0]

        # solve
        start = time.time()
        solved = backtracking.backtrackingSearch(unfinished_board, 0, 0)
        end = time.time()
        func_time = end - start

        # time updates
        if solved:
            num_solved += 1
            total_time += func_time
            avg_time += func_time
        else:
            total_time += func_time

    solve_rate = num_solved / num_iterations
    avg_time = total_time / num_iterations

    print("Clues:", num_clues)
    print("\tSuccess rate:   ", solve_rate*100, "%\n\tAvg solve time: ", avg_time, " sec", sep='')

real_end = time.time()
real_time = real_end - real_start

print("\n", num_iterations * num_types, " boards solved in ", real_time, " seconds.", sep='')
    