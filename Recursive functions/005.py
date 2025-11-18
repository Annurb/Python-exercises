def solveNQueens(n):
    solutions = []
    board = [["."] * n for _ in range(n)]

    def is_safe(row, col):
        # Check vertical
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # Check left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # Check right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row):
        if row == n:
            solution = ["".join(r) for r in board]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return solutions

# Example for N=4
for sol in solveNQueens(6):
    for row in sol:
        print(row)
    print()
