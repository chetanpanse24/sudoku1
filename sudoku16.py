"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-G must occur exactly once in each row.
Each of the digits 1-G must occur exactly once in each column.
Each of the digits 1-G must occur exactly once in each of the
 16 4*4 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
"""
board = [[".", "9", ".", ".", "2", ".", "3", "8", "A", ".", ".", ".", ".", ".", ".", "."],
    [".", "1", ".", "6", ".", ".", "D", ".", ".", ".", "8", ".", "F", ".", "B", "5"],
    [".", ".", ".", "3", ".", "B", ".", ".", ".", "5", ".", ".", "G", ".", ".", "."],
    ["7", ".", ".", "F", ".", ".", ".", "A", ".", ".", "G", "1", ".", "4", ".", "."],
    ["G", ".", ".", ".", ".", ".", ".", "D", ".", "A", "C", "7", ".", ".", ".", "F"],
    [".", ".", ".", ".", "1", "3", ".", "F", ".", "B", ".", "8", ".", ".", ".", "."],
    ["1", "8", ".", "A", ".", ".", ".", "E", ".", ".", ".", ".", "2", ".", ".", "6"],
    ["5", ".", ".", ".", ".", ".", ".", ".", ".", "D", ".", ".", "E", "G", "4", "1"],
    ["9", ".", ".", ".", "E", ".", ".", ".", "7", "1", ".", ".", ".", "A", ".", "4"],
    [".", ".", ".", ".", ".", ".", "1", ".", ".", "9", ".", "E", "C", ".", "8", "."],
    [".", "2", "C", "D", ".", ".", "7", ".", "4", ".", ".", ".", ".", "E", "5", "."],
    [".", "4", ".", ".", ".", ".", ".", ".", ".",  ".", "D", "6", ".", ".", ".", "G"],
    [".", ".", ".", ".", "F", "8", "B", "4", ".", ".", ".", "2", "A", ".", ".", "."],
    ["E", "3", ".", ".", "9", "7", ".", ".", "6", ".", ".", ".", ".", ".", ".", "."],
    [".", "F", "8", "4", ".", ".", "A", ".", ".", ".", "5", ".", "6", ".", ".", "9"],
    [".", ".", ".", ".", ".", "2", ".", "1", "8", ".", ".", "B", ".", ".", ".", "D"]]


"""check in row column and box"""


def check_row(board, row, num):
  for i in range(0, 16):
    if(board[row][i] == num):
      return False
  return True


def check_col(board, col, num):
  for i in range(0, 16):
    if(board[i][col] == num):
        return False
  return True


def check_box(board, row, col, num):
  for i in range(0, 4):
    for j in range(0, 4):
      if(board[row + i][col + j] == num):
        return False
  return True


# solution method
def solution(row=0, col=0):
    if row == 16:
        return True
    elif col >= 16:
        return solution(row+1, 0)
    elif board[row][col] != '.':
        return solution(row, col+1)
    else:
      for num in range(1, 17):
        if (check_row(board, row, str(num)) and check_col(board, col, str(num)) and check_box(board, row - row % 4, col - col % 4, str(num))):
          board[row][col] = str(num)
          if solution(row, col+1):
              return True
    board[row][col] = '.'
    return False


solution()


for i in board:
    print(i)
