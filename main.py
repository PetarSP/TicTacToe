import sys

from winning_condition import winning_condition
from constants import *
from drawings import *
from console_board import *

pygame.init()

player = 1
game_over = False


def restart():
    screen.fill(SCREEN_COLOR)
    draw_lines()
    player = 1
    for rows in range(BOARD_ROWS):
        for cols in range(BOARD_COLS):
            board[rows][cols] = 0


# main loop

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # link console board to pygame board
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // NEEDED_SPACE)
            clicked_col = int(mouseX // NEEDED_SPACE)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if winning_condition(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if winning_condition(player):
                        game_over = True
                    player = 1
            draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
    draw_lines()
