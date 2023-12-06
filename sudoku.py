import random
import copy
import sudoku_backtracking


def sudoku_formula(rVar, cVar):
    value = (3 * (rVar % 3) + rVar // 3 + cVar) % 9
    return value


# changed this to be 3 numbers
mixed_sudoku_amount = [0, 1, 2]
random.shuffle(mixed_sudoku_amount)
# I changed the dict to have the numbers 1-9 without changing any of the math logic
sudoku_dict = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}


def initialize_full_board():
    # initialize base list of possible numerical values
    full_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(full_list)

    # initialize basic row (this code only mixes rows within the same 4 row/column subsection to ensure that the validity of the board is upheld)
    rows = []
    for x in mixed_sudoku_amount:
        for y in mixed_sudoku_amount:
            rows.append(x * 3 + y)

    # initialize basic column (same as row)
    columns = rows.copy()

    # build completed board
    board = []
    for x in rows:
        row_values = []
        for y in columns:
            value = full_list[sudoku_formula(x, y)]
            row_values.append(value)
        board.append(row_values)

    # change values to sudoku values
    for i in range(9):
        for j in range(9):
            if board[i][j] in sudoku_dict.keys():
                board[i][j] = sudoku_dict[board[i][j]]

    return board


def initalize_partial_board(board, spaces):
    # board is a board passed through that was created with the initialize_full_board() function
    # spaces is the number of filled in spaces the sudoku board should start with

    partial_board = copy.deepcopy(board)

    # initialize list of possible row indecies (shuffled)
    rows_indecies = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(rows_indecies)

    # initialize list of possible column indecies (shuffled)
    columns_indecies = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(columns_indecies)

    # replace filled in spaces with _ at random
    empty_spaces = 81 - spaces
    while empty_spaces != 0:
        current_space = (random.choice(rows_indecies), random.choice(columns_indecies))
        x, y = current_space
        if partial_board[x][y] != '_':
            partial_board[x][y] = '_'
            empty_spaces -= 1

    # returns the list [partially completed board, fully completed board]
    return [partial_board, board]


completed_board = initialize_full_board()
unfinished_board = initalize_partial_board(completed_board, 50)[0]
print('Completed board:\n')
for row in completed_board:
    print(row)

print('\n')

print('Unfinished board:\n')
for row in unfinished_board:
    print(row)

if (sudoku_backtracking.backtrackingSearch(unfinished_board, 0, 0)):
    print("\n\nSolved Board:\n")
    for row in unfinished_board:
        print(row)
else:
    print("\nCould not solve.")