import sys
import hexadoku
import cultural_genetic_algo

###
 #  Implementation of a hexadoku solver which employs a cultural genetic algorithm using 
 #  cultural_genetic_algo.py. The algorithm generates a population of boards or 'individuals' 
 #  which are filled with random values, then progressively improves the population by selecting 
 #  individuals to reproduce, then replacing the individuals with the worst fitness values with 
 #  the new offspring. Crossover and mutation is implemented for each new offspring.
 #  This process is repeated until an individual contains a valid solution to the puzzle.
###

# default parameter values
num_boards = 1
num_clues = 205
population_size = 50
num_offspring = 3
num_mutations = 3

# Check if command-line arguments are provided
if len(sys.argv) < 6:
    print("Usage: cga_solver.py num_boards num_clues population_size num_offspring num_mutations")
    print("Using default values: 1 205 50 3 3\n")
else:
    num_boards = int(sys.argv[1])
    num_clues = int(sys.argv[2])
    population_size = int(sys.argv[3])
    num_offspring = int(sys.argv[4])
    num_mutations = int(sys.argv[5])

num_spaces = 256 - num_clues

# initialize board
solution = hexadoku.initialize_full_board()
starting_board = hexadoku.initialize_partial_board(solution, num_clues)[0]

# Print empty board
print("Empty Board:")
for i in range (0, 16):
    print(starting_board[i])
print("-----")

# Create first generation
individuals = cultural_genetic_algo.initialize(starting_board, population_size)

# Check if the first generation solved the board
solved_board = None
for i in range (population_size):
        if individuals[i][1] == 0:
            solved_board = individuals[i][0]

# Iterate until solution is found
iterations = 0
while solved_board == None:

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
    #print(individuals[-1][1])
        
    iterations += 1

print("Solved in", iterations, "generations.")

# Print solution
for i in range (0, 16):
    print(solved_board[i])
if (solved_board == solution):
    print("Found intended solution.")