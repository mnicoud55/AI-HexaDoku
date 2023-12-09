import hexadoku
import backtracking
import time

###
 #  The user selects the range of board types to test and the number of iterations n
 #  to run each board type. The solver runs each board between the upper and lower bound 
 #  n times and prints the success rate and average solving time of each type.
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

    print(avg_time)

real_end = time.time()
real_time = real_end - real_start

print("\n", num_iterations * num_types, " boards solved in ", real_time, " seconds.", sep='')
    