import random

# We used the following stack overflow article as reference for initializing a correct HexaDoku board that has a solution:
# https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

def hexadoku_formula(rows, columns): 
    value = (4 * (rows % 4) + rows // 4 + columns) % 16
    return value

mixed_hex_amount = [0, 1, 2, 3]
random.shuffle(mixed_hex_amount)
hex_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13:'D', 14:'E', 15:'F', 16: 0}

def initialize_full_board():

    # initialize base list of possible numerical values
    full_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(full_list)

    # initialize basic row
    rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(rows)
 
    # initialize basic column
    columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    random.shuffle(columns)

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

current_board = initialize_full_board()
for row in current_board: 
    print(row)


