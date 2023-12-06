import random
import copy
import backtracking

# We used the following stack overflow article as reference for initializing a correct HexaDoku board that has a solution:
# https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python


def hexadoku_formula(rVar, cVar): 
    value = (4 * (rVar % 4) + rVar // 4 + cVar) % 16
    return value


mixed_hex_amount = [0, 1, 2, 3]
random.shuffle(mixed_hex_amount)
hex_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13:'D', 14:'E', 15:'F', 16: 0}


def initialize_full_board():

    # initialize base list of possible numerical values
    full_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(full_list)

    # initialize basic row (this code only mixes rows within the same 4 row/column subsection to ensure that the validity of the board is upheld)
    rows = []
    for x in mixed_hex_amount:
        for y in mixed_hex_amount:
            rows.append(x * 4 + y)
 
    # initialize basic column (same as row)
    columns = rows.copy()

    # build completed board
    board = []
    for x in rows:
        row_values = []
        for y in columns:
            value = full_list[hexadoku_formula(x, y)]
            row_values.append(value)
        board.append(row_values)

    # change double digit numerical values to hex
    for i in range(16):
        for j in range(16):
            if board[i][j] in hex_dict.keys():
                board[i][j] = hex_dict[board[i][j]]

    return board


def initialize_partial_board(board, spaces):
    # board is a board passed through that was created with the initialize_full_board() function
    # spaces is the number of filled in spaces the HexaDoku board should start with

    partial_board = copy.deepcopy(board)

    # initialize list of possible row indices (shuffled)
    rows_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(rows_indices)

    # initialize list of possible column indices (shuffled)
    columns_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(columns_indices)

    # replace filled in spaces with _ at random
    empty_spaces = 256 - spaces
    while empty_spaces != 0:
        current_space = (random.choice(rows_indices), random.choice(columns_indices))
        x, y = current_space
        if partial_board[x][y] != '_':
            partial_board[x][y] = '_'
            empty_spaces -= 1

    # returns the list [partially completed board, fully completed board]
    return [partial_board, board]   


completed_board = initialize_full_board()
unfinished_board = initialize_partial_board(completed_board, 150)[0]
print('Completed board:\n')
for row in completed_board: 
    print(row)

print('\n')

print('Unfinished board:\n')
for row in unfinished_board: 
    print(row)
    
if backtracking.backtrackingSearch(unfinished_board, 0, 0):
    print("\n\nSolved Board:\n")
    for row in unfinished_board: 
        print(row)
else:
    print("\nCould not solve.")


