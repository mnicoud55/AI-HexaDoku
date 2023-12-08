import random
import copy
import backtracking
import hexadoku

### 
 #  Generates a hexadoku board and solves it using backtracking
###

mixed_hex_amount = [0, 1, 2, 3]
random.shuffle(mixed_hex_amount)
hex_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13:'D', 14:'E', 15:'F', 16: 0}

completed_board = hexadoku.initialize_full_board()
unfinished_board = hexadoku.initialize_partial_board(completed_board, 150)[0]
print('Completed board:\n')
hexadoku.print_board(completed_board)

print('\n')

print('Unfinished board:\n')
hexadoku.print_board(unfinished_board)
    
if backtracking.backtrackingSearch(unfinished_board, 0, 0):
    print("\n\nSolved Board:\n")
    hexadoku.print_board(unfinished_board)
else:
    print("\nCould not solve.")
