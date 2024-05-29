def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe.
  """
  # Check row and column
  for i in range(len(board)):
    if board[row][i] == 1 or board[i][col] == 1:
      return False

  # Check diagonals
  for i in range(len(board)):
    for j in range(len(board)):
      if abs(row - i) == abs(col - j) and board[i][j] == 1:
        return False
  return True

def solve_n_queens(board, col):
  """
  Solves the N-Queens problem using backtracking.
  """
  if col >= len(board):
    return True

  for i in range(len(board)):
    if is_safe(board, i, col):
      board[i][col] = 1
      if solve_n_queens(board, col + 1):
        return True
      board[i][col] = 0  # Backtrack

  return False

def print_board(board):
  """
  Prints the chessboard with queens.
  """
  for row in board:
    for col in row:
      print("Q" if col else ".", end=" ")
    print()

# Get user input for n
while True:
  try:
    n = int(input("Enter the number of queens (positive integer): "))
    if n <= 0:
      raise ValueError
    break
  except ValueError:
    print("Invalid input. Please enter a positive integer.")

# Create an empty chessboard
board = [[0 for _ in range(n)] for _ in range(n)]

# Solve the problem and print solutions
if solve_n_queens(board, 0):
  print("Solution:")
  print_board(board)
else:
  print("No solution exists for", n, "queens.")