import sys
import sudoku
import sudoku_cga

###
 #  Implementation of a sudoku solver which employs a cultural genetic algorithm using 
 #  sudoku_cga.py. The algorithm generates a population of boards or 'individuals' 
 #  which are filled with random values, then progressively improves the population by selecting 
 #  individuals to reproduce, then replacing the individuals with the worst fitness values with 
 #  the new offspring. Crossover and mutation is implemented for each new offspring.
 #  This process is repeated until an individual contains a valid solution to the puzzle.
###

# default parameter values
num_boards = 1
num_clues = 34
population_size = 50
num_offspring = 10
num_mutations = 3

# Check if command-line arguments are provided
if len(sys.argv) < 6:
    print("Usage: cga_solver.py num_boards num_clues population_size num_offspring num_mutations")
    print("Using default values: 1 34 50 3 3\n")
else:
    num_boards = int(sys.argv[1])
    num_clues = int(sys.argv[2])
    population_size = int(sys.argv[3])
    num_offspring = int(sys.argv[4])
    num_mutations = int(sys.argv[5])

num_spaces = 81 - num_clues
for _ in range (num_boards): 
    # initialize board
    solution = sudoku.initialize_full_board()
    starting_board = sudoku.initialize_partial_board(solution, num_clues)[0]

    # Print empty board
    print("Starting Board:")
    sudoku.print_board(starting_board)

    # Create first generation
    individuals = sudoku_cga.initialize(starting_board, population_size)

    # Check if the first generation solved the board
    solved_board = None
    for i in range (population_size):
            if individuals[i][1] == 0:
                solved_board = individuals[i][0]


    # Iterate until solution is found
    iterations = 0
    while solved_board is None:

        # Select boards for reproduction
        winners = sudoku_cga.tournament(individuals, 25, num_offspring)

        # Create offspring
        children = []
        for j in range (0, num_offspring*2, 2):
            children.append(sudoku_cga.reproduce(starting_board, winners[j], winners[j+1], num_spaces, num_mutations))

        # Replace worst fitting boards with the new offspring
        individuals = sudoku_cga.replace(individuals, children)

        # Check if the solution has been found
        if individuals[-1][1] == 0:
            solved_board = individuals[-1][0]


        # Uncomment to view fitness progress during runtime
        fit = individuals[-1][1]
        if fit == 0:
            print("\r", fit, " ", sep='')
        else:
            print("\r", fit, " ", sep='', end='')

        iterations += 1

    # Print solution
    sudoku.print_board(solved_board)
    print("Solved in", iterations, "generations.")
    if (solved_board == solution):
        print("Found intended solution.")