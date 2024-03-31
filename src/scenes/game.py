import random

import pygame

from src.constants import PLAYER_INITIAL_POSITION, PLAYER_SIZE, INTENSE_TEMPERATURE_CELL_SIZE, \
    GENERATION_PROBABILITY, MINIMAL_TIME_BEFORE_CELL_GENERATION, THERMOMETER_POSITION, \
    MAX_TEMPERATURE, MIN_TEMPERATURE, DELAY_BEFORE_GAME_OVER
from src.entities.intense_temperature_cell import IntenseTemperatureCell, IntenseTemperatureNature
from src.entities.player import Player
from src.gui.thermometer import Thermometer
from src.scenes.game_over import GameOver
from src.scenes.scene import Scene


class Game(Scene):
    INTENSE_CELL_COLUMNS_NUMBER = 6

    def __init__(self, screen):
        super().__init__(screen)
        self.player: Player = Player(PLAYER_INITIAL_POSITION, PLAYER_SIZE,
                                     "assets/player_cell.png")
        self.intense_temperature_cells: list[IntenseTemperatureCell] = []
        self.temperature = MAX_TEMPERATURE // 2
        self.thermometer = Thermometer(THERMOMETER_POSITION)
        self.double_movement_key_pressed: bool = False
        self.timer_until_next_cell_generation = 0
        self.game_over = False
        self.timer_until_next_scene = DELAY_BEFORE_GAME_OVER

    def _generate_intense_temperature_cell(self) -> bool:
        free_columns = list(range(Game.INTENSE_CELL_COLUMNS_NUMBER))
        for cell in self.intense_temperature_cells:
            if cell.column_index in free_columns and cell.is_position_nearby_spawn():
                free_columns.remove(cell.column_index)

        if len(free_columns) == 0:
            return False

        column_index = random.choice(free_columns)
        nature = random.choice(list(IntenseTemperatureNature))
        self.intense_temperature_cells.append(
            IntenseTemperatureCell(INTENSE_TEMPERATURE_CELL_SIZE, nature,
                                   column_index))
        return True

    def update(self):
        super().update()
        if not self.game_over:
            self.player.update(self.screen)
            self._update_intense_temperature_cells()
            self._check_cell_generation()
            self._check_game_over()

    def _update_intense_temperature_cells(self):
        alive_intense_temperature_cells = []
        for cell in self.intense_temperature_cells:
            if cell.rect.colliderect(self.player):
                cell.alive = False
                self.temperature += cell.temperature_power
            cell.update(self.screen)
            if cell.alive:
                alive_intense_temperature_cells.append(cell)
        self.intense_temperature_cells = alive_intense_temperature_cells

    def _check_cell_generation(self):
        if self.timer_until_next_cell_generation <= 0:
            should_generate_cell = random.random() < GENERATION_PROBABILITY
            if should_generate_cell and self._generate_intense_temperature_cell():
                self.timer_until_next_cell_generation = MINIMAL_TIME_BEFORE_CELL_GENERATION
        else:
            self.timer_until_next_cell_generation -= 1

    def draw(self):
        super().draw()
        if not self.game_over:
            self.player.display(self.screen)
        for cell in self.intense_temperature_cells:
            cell.display(self.screen)
        self.thermometer.display(self.screen, self.temperature)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_f:
                if self.player.in_movement:
                    self.double_movement_key_pressed = True
                else:
                    self.player.in_movement = True
                self.player.move_left = event.key == pygame.K_s
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_f:
                if self.double_movement_key_pressed:
                    self.double_movement_key_pressed = False
                else:
                    self.player.in_movement = False

    def _check_game_over(self):
        self.game_over = self.temperature not in range(MIN_TEMPERATURE, MAX_TEMPERATURE)
        if self.game_over:
            self.next_scene = GameOver(self.screen)
