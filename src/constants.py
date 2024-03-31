import pygame

GAME_TITLE = "Stay in the norms"

MAIN_WIN_WIDTH = 600
MAIN_WIN_HEIGHT = 800
PLAYER_SIZE = (50, 50)
PLAYER_INITIAL_POSITION = (MAIN_WIN_WIDTH // 2 - PLAYER_SIZE[0] // 2,
                           MAIN_WIN_HEIGHT - PLAYER_SIZE[1] - 20)

FRAME_RATE = 60

# Colors
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
LIGHT_YELLOW = pygame.Color("yellow")
