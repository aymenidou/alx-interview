#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    '''check if there is a queen in the same or diagonal column'''
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N, row, board, solutions):
    '''backtracking the queens'''
    if row == N:
        solutions.append(board.copy())
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1  # Backtrack


def print_solutions(N, solutions):
    '''print the solutions found'''
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])


def nqueens(N):
    '''check the arguments and initiate the backtracking'''
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(N, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
