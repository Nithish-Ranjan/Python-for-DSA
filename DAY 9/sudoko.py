def is_safe(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


board = []

print("Enter Sudoku (use 0 for empty cells):")
for i in range(9):
    board.append(list(map(int, input().split())))

if solve(board):
    print("\nSolved Sudoku:")
    for row in board:
        print(*row)
else:
    print("No solution exists.")