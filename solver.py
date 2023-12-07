import hexadoku
import backtracking
import time

###
 #  Records the time and success rate of the backtracking algorithm over n hexadoku 
 #  boards each starting with m clues (prefilled cells), given n and m as input
###

num_clues = int(input("Enter number of clues (0-255): "))
num_iterations = int(input("Enter number of iterations: "))
num_solved = 0
total_time = 0
avg_time = 0

real_start = time.time()
for i in range (num_iterations):

    # initialize board
    completed_board = hexadoku.initialize_full_board()
    unfinished_board = hexadoku.initialize_partial_board(completed_board, num_clues)[0]

    # solve
    start = time.time()
    solved = backtracking.backtrackingSearch(unfinished_board, 0, 0)
    end = time.time()
    func_time = end - start

    # time updates and progress bar
    if solved:
        num_solved += 1
        total_time += func_time
        avg_time += func_time
        if i == num_iterations - 1 or (i%10 == 0 and i > 0):
            print("|")
        else:
            print("|", end =" ", flush=True)
    else:
        total_time += func_time
        if i == num_iterations - 1 or (i%10 == 0 and i > 0):
            print("X")
        else:
            print("X", end =" ", flush=True)

real_end = time.time()

real_time = real_end - real_start
solve_rate = num_solved / num_iterations
avg_time = total_time / num_iterations

print(num_iterations, " boards solved in ", real_time, " seconds (", total_time, " function time).", sep='')
print("Success rate: ", solve_rate*100, "%\nAverage solving time: ", avg_time, " seconds", sep='')