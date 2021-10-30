import numpy as np

from drawings import *
from constants import *

board = np.zeros((BOARD_ROWS, BOARD_COLS))


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True



