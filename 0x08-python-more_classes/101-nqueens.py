import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append([(i, board[i].index(1)) for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0


def nqueens_positions(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for k in range(n)] for k in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for i in range(len(solutions)):
        for j in range(len(solutions[i])):
            solutions[i][j] = list(solutions[i][j])
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens_positions.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solutions = nqueens_positions(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
