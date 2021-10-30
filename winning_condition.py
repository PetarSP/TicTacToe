from drawings import *
from console_board import *

def winning_condition(player):
    # vertical condition
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # horizontal condition
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # secondary diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_primary_diagonal_winning_line(player)
        return True
    # primary diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_secondary_diagonal_winning_line(player)
        return True
    return False
