# import hexadoku
# N is the size of the 2D matrix   N*N
N = 16
hex_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13:'D', 14:'E', 15:'F', 16: 0}
 
def isConsistent(grid, row, col, num):
    # check row constraint
    for x in range(N):
        if grid[row][x] == num:
            return False
        
    # check column constraint
    for x in range(N):
        if grid[x][col] == num:
            return False

    # check 4x4 region constraint
    for i in range(4):
        for j in range(4):
            if grid[i + row - row % 4][j + col - col % 4] == num:
                return False
            
    return True
 

def backtrackingSearch(grid, row, col):
    # base case: if we have reached the end of the board, return True
    if (row >= N - 1 and col >= N):
        return True

    # if at the end of the columns, move on to the next row
    if col == N:
        col = 0
        row += 1
 
    # if the value stored in [row][col] is filled in, move on to the next column
    if grid[row][col] != '_':
        return backtrackingSearch(grid, row, col + 1)
    
    for num in range(N):
        if isConsistent(grid, row, col, hex_dict[num]):
            grid[row][col] = hex_dict[num]
            if backtrackingSearch(grid, row, col + 1):
                return True
        grid[row][col] = '_'
    return False