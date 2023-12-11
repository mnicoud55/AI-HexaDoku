import sys
import hexadoku
import cultural_genetic_algo
import time

###
 #  Implementation of a hexadoku solver which employs a cultural genetic algorithm using 
 #  cultural_genetic_algo.py. The algorithm generates a population of boards or 'individuals' 
 #  which are filled with random values, then progressively improves the population by selecting 
 #  individuals to reproduce, then replacing the individuals with the worst fitness values with 
 #  the new offspring. Crossover and mutation is implemented for each new offspring.
 #  This process is repeated until an individual contains a valid solution to the puzzle.
###

# default parameter values
num_boards = 5
num_clues = 205
population_size = 300
num_offspring = 12
num_mutations = 3

upper_bound = 197
lower_bound = 193

# Check if command-line arguments are provided
if len(sys.argv) < 6:
    print("Usage: cga_solver.py num_boards num_clues population_size num_offspring num_mutations")
    print("Using default values:", num_boards, num_clues, population_size, num_offspring, num_mutations, "\n")
else:
    num_boards = int(sys.argv[1])
    num_clues = int(sys.argv[2])
    population_size = int(sys.argv[3])
    num_offspring = int(sys.argv[4])
    num_mutations = int(sys.argv[5])

num_spaces = 256 - num_clues

for num_clues_range in range(upper_bound, lower_bound-1, -1):
    num_solved = 0
    total_time = 0
    avg_time = 0
    total_same = 0
    same_time = 0
    max_time = 0

    avg_generations = 0
    max_iterations = 0

    num_spaces = 256 - num_clues_range

    for _ in range(num_boards):

        # initialize board
        solution = hexadoku.initialize_full_board()
        starting_board = hexadoku.initialize_partial_board(solution, num_clues_range)[0]

        # Print empty board
        # print("Starting Board:")
        # hexadoku.print_board(starting_board)
        # print("Solution:")
        # hexadoku.print_board(solution)

        start = time.time()
        # Create first generation
        individuals = cultural_genetic_algo.initialize(starting_board, population_size)
        # Check if the first generation solved the board
        solved_board = None
        for i in range (population_size):
                if individuals[i][1] == 0:
                    solved_board = individuals[i][0]


        # Iterate until solution is found
        iterations = 1
        while solved_board is None:

            # Select boards for reproduction
            winners = cultural_genetic_algo.tournament(individuals, 25, num_offspring)

            # Create offspring
            children = []
            for j in range (0, num_offspring*2, 2):
                children.append(cultural_genetic_algo.reproduce(starting_board, winners[j], winners[j+1], num_spaces, num_mutations))

            # Replace worst fitting boards with the new offspring
            individuals = cultural_genetic_algo.replace(individuals, children)

            # Check if the solution has been found
            if individuals[-1][1] == 0:
                solved_board = individuals[-1][0]


            # Uncomment to view fitness progress during runtime
            fit = individuals[-1][1]
            # if fit == 0:
            #     print("\r", fit, " ", sep='')
            # else:
            #     print("\r", fit, " ", sep='', end='')

            iterations += 1
        end = time.time()
        t = end - start

        if solved_board:
            num_solved += 1
            total_time += t
            avg_time += t
            avg_generations += iterations
            if solved_board == solution:
                total_same += 1
                same_time += t
            if t > max_time:
                max_time = t
            if iterations > max_iterations:
                max_iterations = iterations

    solve_rate = num_solved / num_boards
    avg_time = total_time / num_boards

    avg_same_time = same_time / (total_same + 0.0000001)
    avg_generations = avg_generations / num_boards

    print(num_clues_range, avg_time, max_time, avg_same_time, total_same, "/", num_boards, avg_generations, max_iterations)
        # # Print solution
        # hexadoku.print_board(solved_board)
        # print(iterations, t)
        # if (solved_board == solution):
        #     print("Found intended solution.")

