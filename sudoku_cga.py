import sudoku
import random

###
 #  Functions for a sudoku solver which employs a cultural genetic algorithm.
 #  The algorithm generates a population of boards or 'individuals' which are filled with
 #  random values, then progressively improves the population by selecting individuals to
 #  reproduce, then replacing the individuals with the worst fitness values with the new 
 #  offspring. Crossover and mutation is implemented for each new offspring.
 #  This process is repeated until an individual contains a valid solution to the puzzle.
###

grids = [ 
        [ 0, 0, 0, 1, 1, 1, 2, 2, 2],
        [ 0, 0, 0, 1, 1, 1, 2, 2, 2],
        [ 0, 0, 0, 1, 1, 1, 2, 2, 2],
        [ 3, 3, 3, 4, 4, 4, 5, 5, 5],
        [ 3, 3, 3, 4, 4, 4, 5, 5, 5],
        [ 3, 3, 3, 4, 4, 4, 5, 5, 5],
        [ 6, 6, 6, 7, 7, 7, 8, 8, 8],
        [ 6, 6, 6, 7, 7, 7, 8, 8, 8],
        [ 6, 6, 6, 7, 7, 7, 8, 8, 8]
         ]

def initialize(board, population):
    ###
     #  Initializes a population of boards filled with random values from the given incomplete board.
     #  The random values adhere to the belief space, i.e. they must be digits 0-9 and aren't repetitions
     #  of the clues given in each row, column, and grid 
    ###
    individuals = []
    for i in range (population):
        # Make a copy of the empty board
        indiv = [[None] * 9 for _ in range(9)]
        for i in range (0, 9):
             for j in range (0, 9):
                 indiv[i][j] = board[i][j]

        # Fill board with values
        for j, row in enumerate(board):
            for k, col in enumerate(board[j]):
                if board[j][k] == '_':
                    indiv[j][k] = generate_gene(j, k, board)
        fit = get_fitness(indiv)
        individuals.append(fit)
        
    return individuals
                
def generate_gene(rowPos, colPos, board):
    ###
     #  Generates a random digit for a cell that doesn't
     #  repeat any clues that are in its row, column, or grid.
    ###
    pos_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # get the row, column, and grid into their own lists
    attributes = get_attributes(board)
    row = attributes["rows"][rowPos]
    col = attributes["cols"][colPos]
    gridNum = grids[rowPos][colPos]
    grid = attributes["grids"][gridNum]

    # Eliminate digits that would violate belief space
    for val in row:
        if val in pos_values:
            pos_values.remove(val)
    for val in col:
        if val in pos_values:
            pos_values.remove(val)
    for val in grid:
        if val in pos_values:
            pos_values.remove(val)
    
    return random.choice(pos_values)
    
def tournament(individuals, tourney_size, num_offspring):
    ###
     #  Selects a subpopulation from the individuals and performs a 
     #  deterministic tournament selection on that subpopulation.
    ###
    num_winners = 2*num_offspring

    # Select competitors at random
    competitors = random.sample(individuals, tourney_size)
    competitors = sorted(competitors, key=lambda x: x[1])

    # Select the boards with the best fitness
    #sorted_indivs = sorted(individuals, key=lambda x: x[1])
    #competitors = sorted_indivs[0:tourney_size]

    winners = []
    for i in range (num_winners):
        winners.append(competitors[i])
    
    return winners

def get_fitness(board):
    ###
     #  Calculates fitness of the given board.
     #  Fitness is the number of errors (repetitions), so a low fitness is better.
     #  A fitness of 0 means that the board is solved.
    ###
    attributes = get_attributes(board)
    fitness = 0
    for row in attributes["rows"]:
        fitness += len(row) - len(set(row))
    for col in attributes["cols"]:
        fitness += len(col) - len(set(col))
    for grid in attributes["grids"]:
        fitness += len(grid) - len(set(grid))

    return (board, fitness)
            
def get_attributes(board):
    ###
     #  Returns a dict containing every row, column, and grid in 
     #  the given board so they can be easily iterated through.
    ###
    attributes = {
        "rows": [[], [], [], [], [], [], [], [], []], 
        "cols": [[], [], [], [], [], [], [], [], []], 
        "grids":[[], [], [], [], [], [], [], [], []]
        }

    for i, row in enumerate(board):
        attributes["rows"][i] = row
        for j, col in enumerate(board[i]):
            attributes["cols"][j].append(col)
            grid = grids[i][j]
            attributes["grids"][grid].append(col)
    return attributes

def reproduce(starting_board, board1, board2, spaces, num_mutations):
    ###
     #  Creates an offspring from the 2 parent boards. 
     #  Single point, simple crossover is implemented, which selects a random value
     #  between 1 and the number of empty cells. The child is constructed with
     #  values from parent 1 for all the spaces before the generated value, and all the
     #  cells following the value are taken from parent 2.
     # 
     #  The child also undergoes mutation, which randomly selects cells and assigns 
     #  them random values (which comply with the belief space)
    ###
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    child = [[None] * 9 for _ in range(9)]

    # get crossover value
    crossover = random.randint(1, spaces)

    # generate mutations
    mutations = []
    for i in range (num_mutations):
        mutations.append((random.randint(0, spaces-1), random.choice(values)))
        mutations = sorted(mutations, key=lambda x: x[0])

    # Construct child
    space_num = 0
    for r in range (0, 9):
        for c in range (0, 9):
            if len(mutations) > 0 and space_num == mutations[0][0]:
                child[r][c] = mutations[0][1]
                mutations.pop(0)
            else:
                if starting_board[r][c] == '_':
                    space_num += 1
                if space_num < crossover:
                    child[r][c] = board1[0][r][c]
                else:
                    child[r][c] = board2[0][r][c]
    return get_fitness(child)
            
def replace(individuals, new_indivs):
    ###
     #  Replaces the boards with the worst fitness with the newly generated boards
    ###
    n = len(new_indivs)
    for i in range(n):
        individuals.append(new_indivs[i])
    sorted_indivs = sorted(individuals, key=lambda x: x[1], reverse=True)
    for i in range(n):
        sorted_indivs.pop(0)
    
    return sorted_indivs
