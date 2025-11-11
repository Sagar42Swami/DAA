def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def is_safe(board, row, col, n):
    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if board[row][col] == 1:
            # Skip the first placed queen
            if solve_nqueens(board, col + 1, n):
                return True
        elif is_safe(board, row, col, n):
            # Try placing a queen
            board[row][col] = 1
            if solve_nqueens(board, col + 1, n):
                return True
            
            # Backtrack if placing didn't lead to a solution
            board[row][col] = 0

    # If no row in this column works, return False
    return False


# --- Driver Code ---
n = int(input("Enter the size of the board (n): "))
first_row = int(input(f"Enter row index for first queen (0 to {n-1}): "))
first_col = int(input(f"Enter column index for first queen (0 to {n-1}): "))

# Initialize board
board = [[0 for _ in range(n)] for _ in range(n)]
board[first_row][first_col] = 1  # Place first queen

# Solve remaining queens
if solve_nqueens(board, 0, n):
    print("\nFinal n-Queens Matrix:")
    print_board(board)
else:
    print("\nNo solution exists with the given first queen position.")
    