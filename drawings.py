from console_board import *
from constants import *
import pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(SCREEN_COLOR)


def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SCREEN_HEIGHT // 3), (SCREEN_WIDTH, SCREEN_HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SCREEN_HEIGHT // 3 + NEEDED_SPACE),
                     (SCREEN_WIDTH, SCREEN_HEIGHT // 3 + NEEDED_SPACE), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH // 3, 0), (SCREEN_WIDTH // 3, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH // 3 + NEEDED_SPACE, 0),
                     (SCREEN_WIDTH // 3 + NEEDED_SPACE, SCREEN_HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(col * NEEDED_SPACE + NEEDED_SPACE / 2), int(row * NEEDED_SPACE + NEEDED_SPACE / 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * NEEDED_SPACE + SPACE_BETWEEN_LINE_CORNER,
                                                       row * NEEDED_SPACE + NEEDED_SPACE - SPACE_BETWEEN_LINE_CORNER),
                                 (col * NEEDED_SPACE + NEEDED_SPACE - SPACE_BETWEEN_LINE_CORNER,
                                  row * NEEDED_SPACE + SPACE_BETWEEN_LINE_CORNER), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (
                    col * NEEDED_SPACE + SPACE_BETWEEN_LINE_CORNER, row * NEEDED_SPACE + SPACE_BETWEEN_LINE_CORNER),
                                 (col * NEEDED_SPACE + NEEDED_SPACE - SPACE_BETWEEN_LINE_CORNER,
                                  row * NEEDED_SPACE + NEEDED_SPACE - SPACE_BETWEEN_LINE_CORNER), CROSS_WIDTH)


def draw_vertical_winning_line(col, player):
    posX = col * NEEDED_SPACE + NEEDED_SPACE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, SCREEN_HEIGHT - 15), WINNING_LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    posY = row * NEEDED_SPACE + NEEDED_SPACE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (SCREEN_WIDTH - 15, posY), WINNING_LINE_WIDTH)


def draw_primary_diagonal_winning_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, SCREEN_HEIGHT - 15), (SCREEN_WIDTH - 15, 15), WINNING_LINE_WIDTH)


def draw_secondary_diagonal_winning_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15), WINNING_LINE_WIDTH)
