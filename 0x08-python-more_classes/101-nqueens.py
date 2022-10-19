#!/usr/bin/python3
"""N queens problem."""
import sys


def print_board(board):
    """Print a board."""
    print([[i, val] for i, val in enumerate(board)])


def valid(board, column):
    """Check if a board state is possible."""
    if column == 0:
        return True
    for i in range(column):
        if (board[i] - board[column]) / (i - column) in [1, -1, 0]:
            return False
    return True


def nqueens(board, column, n):
    """Find the nqueens solutions possible from this board state."""
    if column == n:
        print_board(board)
        return

    for i in range(n):
        new_board = [item for item in board]
        new_board[column] = i
        if not valid(new_board, column):
            continue
        nqueens(new_board, column + 1, n)


def main():
    """Solve the n queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens([0] * n, 0, n)


if __name__ == '__main__':
    main()
