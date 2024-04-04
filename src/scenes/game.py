import random

import pygame

from src.constants import PLAYER_INITIAL_POSITION, PLAYER_SIZE, INTENSE_TEMPERATURE_CELL_SIZE, \
    GENERATION_PROBABILITY, MINIMAL_TIME_BEFORE_CELL_GENERATION, THERMOMETER_POSITION, \
    MAX_TEMPERATURE, MIN_TEMPERATURE, DELAY_BEFORE_GAME_OVER, SCORE_TEXT, LIGHT_YELLOW, \
    DELAY_BEFORE_SCORE_INCREASE, DEFAULT_SCORE_INCREASE_VALUE, PERFECT_TEMPERATURE, \
    INTENSE_CELL_COLUMNS_NUMBER, GAME_AREA_HORIZONTAL_START, \
    GAME_AREA_HORIZONTAL_END, DELAY_BEFORE_DIFFICULTY_INCREASE
from src.entities.intense_temperature_cell import IntenseTemperatureCell, IntenseTemperatureNature
from src.entities.player import Player
from src.gui import fonts
from src.gui.thermometer import Thermometer
from src.scenes.game_over import GameOver
from src.scenes.scene import Scene

DIFFICULTY_LEVELS = [
    {"generated_cells_range": (1, 2), "amplifier_proportion": 0},
    {"generated_cells_range": (1, 2, 3), "amplifier_proportion": 0.1},
    {"generated_cells_range": (1, 2, 3, 4), "amplifier_proportion": 0.2},
    {"generated_cells_range": (2, 3, 4), "amplifier_proportion": 0.2},
    {"generated_cells_range": (2, 3, 4), "amplifier_proportion": 0.4},
    {"generated_cells_range": (3, 4, 5), "amplifier_proportion": 0.5},
    {"generated_cells_range": (4, 5), "amplifier_proportion": 0.6},
    {"generated_cells_range": (4, 5, 6), "amplifier_proportion": 0.75},
    {"generated_cells_range": (5, 6), "amplifier_proportion": 0.75},
]


class Game(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.player: Player = Player(PLAYER_INITIAL_POSITION, PLAYER_SIZE,
                                     "assets/player_cell.png")
        self.intense_temperature_cells: list[IntenseTemperatureCell] = []
        self.temperature = PERFECT_TEMPERATURE
        self.thermometer = Thermometer(THERMOMETER_POSITION)
        self.score = 0
        self.timer_until_score_increase: int = DELAY_BEFORE_SCORE_INCREASE
        self.double_movement_key_pressed: bool = False
        self.timer_until_next_cell_generation: int = 0
        self.difficulty_level = 0
        self.timer_until_difficulty_increase: int = DELAY_BEFORE_DIFFICULTY_INCREASE
        self.number_generated_cells_range = DIFFICULTY_LEVELS[self.difficulty_level][
            "generated_cells_range"]
        self.amplifiers_proportion = DIFFICULTY_LEVELS[self.difficulty_level][
            "amplifier_proportion"]
        self.game_over = False
        self.timer_until_next_scene = DELAY_BEFORE_GAME_OVER

    def _generate_intense_temperature_cells(self) -> bool:
        cell_quantity_to_generate = random.choice(self.number_generated_cells_range)
        free_columns = list(range(INTENSE_CELL_COLUMNS_NUMBER))
        generated_at_least_one_cell = False
        for cell in self.intense_temperature_cells:
            if cell.column_index in free_columns and cell.is_position_nearby_spawn():
                free_columns.remove(cell.column_index)
        for _ in range(cell_quantity_to_generate):
            if len(free_columns) == 0:
                break

            column_index = random.choice(free_columns)
            if random.random() < self.amplifiers_proportion:
                nature = IntenseTemperatureNature.AMPLIFIER
            else:
                nature = random.choice(
                    [IntenseTemperatureNature.COLD, IntenseTemperatureNature.WARM])
            self.intense_temperature_cells.append(
                IntenseTemperatureCell(INTENSE_TEMPERATURE_CELL_SIZE, nature,
                                       column_index))
            free_columns.remove(column_index)
            generated_at_least_one_cell = True
        return generated_at_least_one_cell

    def update(self):
        super().update()
        if not self.game_over:
            self.player.update(self.screen)
            if self.player.rect.x < GAME_AREA_HORIZONTAL_START:
                self.player.rect.x = GAME_AREA_HORIZONTAL_START
            elif self.player.rect.x > GAME_AREA_HORIZONTAL_END - self.player.rect.width:
                self.player.rect.x = GAME_AREA_HORIZONTAL_END - self.player.rect.width
            self._update_difficulty()
            self._update_intense_temperature_cells()
            self._check_cell_generation()
            self._check_game_over()
            self._update_score()

    def _update_intense_temperature_cells(self):
        alive_intense_temperature_cells = []
        for cell in self.intense_temperature_cells:
            if cell.rect.colliderect(self.player):
                cell.alive = False
                self.temperature += cell.get_temperature_power(self.temperature)
            cell.update(self.screen)
            if cell.alive:
                alive_intense_temperature_cells.append(cell)
        self.intense_temperature_cells = alive_intense_temperature_cells

    def _check_cell_generation(self):
        if self.timer_until_next_cell_generation <= 0:
            should_generate_cell = random.random() < GENERATION_PROBABILITY
            if should_generate_cell and self._generate_intense_temperature_cells():
                self.timer_until_next_cell_generation = MINIMAL_TIME_BEFORE_CELL_GENERATION
        else:
            self.timer_until_next_cell_generation -= 1

    def _update_score(self):
        if self.timer_until_score_increase <= 0:
            self.timer_until_score_increase = DELAY_BEFORE_SCORE_INCREASE
            self.score += DEFAULT_SCORE_INCREASE_VALUE - self._compute_temperature_shift_penalty()
        else:
            self.timer_until_score_increase -= 1

    def _compute_temperature_shift_penalty(self):
        return abs(self.temperature - PERFECT_TEMPERATURE) // 5 * 5

    def draw(self):
        super().draw()
        if not self.game_over:
            self.player.display(self.screen)
        for cell in self.intense_temperature_cells:
            cell.display(self.screen)
        self.thermometer.display(self.screen, self.temperature)
        score_rendering = fonts.fonts["SCORE_FONT"].render(f"{SCORE_TEXT}: {self.score}",
                                                           True, LIGHT_YELLOW)
        self.screen.blit(score_rendering,
                         (self.screen.get_width() - score_rendering.get_width(), 0))

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_s or event.key == pygame.K_f or
                    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                if self.player.in_movement:
                    self.double_movement_key_pressed = True
                else:
                    self.player.in_movement = True
                self.player.move_left = event.key == pygame.K_s or event.key == pygame.K_LEFT
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_s or event.key == pygame.K_f or
                    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                if self.double_movement_key_pressed:
                    self.double_movement_key_pressed = False
                else:
                    self.player.in_movement = False

    def _check_game_over(self):
        self.game_over = self.temperature not in range(MIN_TEMPERATURE, MAX_TEMPERATURE)
        if self.game_over:
            self.next_scene = GameOver(self.screen, self.score, self.difficulty_level)

    def _update_difficulty(self):
        if (self.timer_until_difficulty_increase <= 0 and
                self.difficulty_level < len(DIFFICULTY_LEVELS) - 1):
            self.difficulty_level += 1
            self.number_generated_cells_range = DIFFICULTY_LEVELS[self.difficulty_level][
                "generated_cells_range"]
            self.amplifiers_proportion = DIFFICULTY_LEVELS[self.difficulty_level][
                "amplifier_proportion"]
            self.timer_until_difficulty_increase = DELAY_BEFORE_DIFFICULTY_INCREASE
        else:
            self.timer_until_difficulty_increase -= 1
