import random
import copy
import sudoku
import sudoku_backtracking

# changed this to be 3 numbers
mixed_sudoku_amount = [0, 1, 2]
random.shuffle(mixed_sudoku_amount)
# I changed the dict to have the numbers 1-9 without changing any of the math logic
sudoku_dict = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}

completed_board = sudoku.initialize_full_board()
unfinished_board = sudoku.initialize_partial_board(completed_board, 50)[0]
print('Completed board:\n')
sudoku.print_board(completed_board)

print('\n')

print('Unfinished board:\n')
sudoku.print_board(unfinished_board)

if sudoku_backtracking.backtrackingSearch(unfinished_board, 0, 0):
    print("\n\nSolved Board:\n")
    sudoku.print_board(unfinished_board)
    if unfinished_board == completed_board:
        print("Solution is the same as completed board")
    else:
        print("Solution is NOT the same as completed board")
else:
    print("\nCould not solve.")