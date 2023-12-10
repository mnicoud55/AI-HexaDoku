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
num_types = upper_bound - lower_bound + 1 # the number was wrong without this
num_iterations = int(input("Iterations per board type: "))
print("")

real_start = time.time()
for num_clues in range (upper_bound, lower_bound-1, -1):
    num_solved = 0
    total_time = 0
    avg_time = 0
    total_same = 0
    same_time = 0
    max_time = 0

    for i in range (num_iterations):

        # initialize board
        completed_board = hexadoku.initialize_full_board()
        unfinished_board = hexadoku.initialize_partial_board(completed_board, num_clues)[0]

        # solve
        start = time.time()
        solved = backtracking.backtrackingSearch(unfinished_board, 0, 0)
        end = time.time()
        func_time = end - start

        same_board = unfinished_board == completed_board
        # time updates
        if solved:
            num_solved += 1
            total_time += func_time
            avg_time += func_time
            if same_board:
                total_same += 1
                same_time += func_time
            if func_time > max_time:
                max_time = func_time

        else:
            total_time += func_time

    solve_rate = num_solved / num_iterations
    avg_time = total_time / num_iterations

    avg_same_time = same_time / (total_same + 0.0000001)

    # print(num_clues, "clues on average takes", avg_time, "seconds with the backtracking algorithm.", total_same, "/", num_iterations, "found the intended solution.")
    # print("   ", avg_same_time, "seconds with the backtracking algorithm for those that found the intended solution")
    # print("   ", max_time, "max time seconds with the backtracking algorithm")

    print(num_clues, avg_time, max_time, avg_same_time, total_same, "/", num_iterations)

real_end = time.time()
real_time = real_end - real_start

print("\n", num_iterations * num_types, " boards solved in ", real_time, " seconds.", sep='')
    