def safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
    if row == n:
        for i in board:
            print(" ".join(i))
        print()
        return

    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = "Q"
            solve(board, row + 1, n)
            board[row][col] = "."

n = int(input("Enter n: "))
board = [["." for _ in range(n)] for _ in range(n)]
solve(board, 0, n)