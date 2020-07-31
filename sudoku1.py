"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.



sudokuGridEasy = [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]


Constraints

The given board contains only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have at least one solution.
The given board size is always 9x9.

Output:

[['5', '3', '4', '6', '7', '8', '9', '1', '2'],
['6', '7', '2', '1', '9', '5', '3', '4', '8'],
['1', '9', '8', '3', '4', '2', '5', '6', '7'],
['8', '5', '9', '7', '6', '1', '4', '2', '3'],
['4', '2', '6', '8', '5', '3', '7', '9', '1'],
['7', '1', '3', '9', '2', '4', '8', '5', '6'],
['9', '6', '1', '5', '3', '7', '2', '8', '4'],
['2', '8', '7', '4', '1', '9', '6', '3', '5'],
['3', '4', '5', '2', '8', '6', '1', '7', '9']

"""
board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

def check_row(board, row, num):  #check in row
   for i in range(0, 9):
       if(board[row][i] == num):
          return False
   return True
def check_col(board, col, num):  # check in column
   for i in range(0, 9):
       if(board[i][col] == num):
          return False
   return True
def check_box(board, row, col, num):  #check in box
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i + row][col + j] == num):
                return False
    return True         



# solution method
def solution(row=0, col=0):
    if row == 9:
        return True  
    elif col >= 9:
        return solution(row+1, 0)
    elif board[row][col]!='.':
        return solution(row, col+1)
    else:    
      for num in range(1,10):
          if (check_row(board, row, str(num)) and check_col(board, col, str(num)) and check_box(board, row - row % 3, col - col % 3, str(num))):
            board[row][col] = str(num)
            if solution(row, col+1):
               return True
            board[row][col] = '.'
    return False


"""
# for input
print("enter the sudoku question and at empty place write "." ")
board []
for i in range(9):
    a []
  for j in range(9):
     a.append(int(input())
  board.append(a)                                                                                        
"""
solution()

for i in board: 
   print(i)
