import pygame

GAME_TITLE = "Stay in the norms"

FRAME_RATE = 60

MAIN_WIN_WIDTH = 600
MAIN_WIN_HEIGHT = 800

MAIN_MENU_WIDTH = 450
HIGH_SCORE_MENU_WIDTH = 500
HELP_MENU_WIDTH = 500
GLOSSARY_MENU_WIDTH = 600
CONTROLS_MENU_WIDTH = 500

GAME_AREA_HORIZONTAL_START = 100
GAME_AREA_HORIZONTAL_END = 500

PLAYER_SIZE = (50, 50)
PLAYER_INITIAL_POSITION = pygame.Vector2(MAIN_WIN_WIDTH // 2 - PLAYER_SIZE[0] // 2,
                                         MAIN_WIN_HEIGHT - PLAYER_SIZE[1] - 20)

INTENSE_TEMPERATURE_CELL_SIZE = (50, 50)
INTENSE_CELL_HORIZONTAL_START = 100
INTENSE_CELL_COLUMNS_NUMBER = 6
HORIZONTAL_GAP_BETWEEN_CELLS = 20
MINIMAL_VERTICAL_GAP_BETWEEN_CELLS = 40

WARNING_SIGN_SIZE = (64, 64)
THERMOMETER_POSITION = pygame.Vector2(10, 300)
MIN_TEMPERATURE = 0
MAX_TEMPERATURE = 100
PERFECT_TEMPERATURE = (MIN_TEMPERATURE + MAX_TEMPERATURE) // 2

MINIMAL_TIME_BEFORE_CELL_GENERATION = FRAME_RATE // 3
GENERATION_PROBABILITY = 0.1
DELAY_BEFORE_DIFFICULTY_INCREASE = FRAME_RATE * 20

DEFAULT_SCORE_INCREASE_VALUE = PERFECT_TEMPERATURE
DELAY_BEFORE_SCORE_INCREASE = FRAME_RATE

DELAY_BEFORE_GAME_OVER = FRAME_RATE * 2

# Colors
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
LIGHT_YELLOW = pygame.Color("yellow")
RED = pygame.Color("#d80d0d")
CRYSTAL_WHITE = pygame.Color("#a1dfe4")
BLUE = pygame.Color("#164bea")

# Text
NEW_GAME_TEXT = "New Game"
HELP_TEXT = "Help"
GLOSSARY_TEXT = "Cell Glossary"
CONTROLS_TEXT = "Controls"
HIGH_SCORE_TEXT = "High Score"
EXIT_GAME_TEXT = "Exit Game"
GAME_OVER_TEXT = "Game Over"
SCORE_TEXT = "Score"
DIFFICULTY_LEVEL_TEXT = "Difficulty level reached"
