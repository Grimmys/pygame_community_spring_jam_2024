import random
from typing import Optional

import pygame

from src.constants import PLAYER_INITIAL_POSITION, PLAYER_SIZE, INTENSE_TEMPERATURE_CELL_SIZE
from src.entities.intense_temperature_cell import IntenseTemperatureCell
from src.entities.player import Player
from src.scenes.scene import Scene


class Game(Scene):
    INTENSE_CELL_COLUMNS_NUMBER = 6

    def __init__(self, screen):
        super().__init__(screen)
        self.player: Player = Player(pygame.Vector2(PLAYER_INITIAL_POSITION), PLAYER_SIZE,
                                     "assets/player_cell.png")
        self.intense_temperature_cells: list[IntenseTemperatureCell] = []
        for _ in range(3):
            cell: Optional[IntenseTemperatureCell] = self._generate_intense_temperature_cell()
            if cell:
                self.intense_temperature_cells.append(cell)
        self.double_movement_key_pressed: bool = False

    def _generate_intense_temperature_cell(self) -> Optional[IntenseTemperatureCell]:
        free_columns = list(range(Game.INTENSE_CELL_COLUMNS_NUMBER))
        for cell in self.intense_temperature_cells:
            if cell.column_index in free_columns and cell.is_position_nearby_spawn():
                free_columns.remove(cell.column_index)

        if len(free_columns) == 0:
            return None

        column_index = random.choice(free_columns)
        return IntenseTemperatureCell(INTENSE_TEMPERATURE_CELL_SIZE, "assets/cold_cell.png",
                                      column_index)

    def update(self):
        super().update()
        self.player.update(self.screen)
        for cell in self.intense_temperature_cells:
            cell.update(self.screen)

    def draw(self):
        super().draw()
        self.screen.fill(pygame.Color("BLACK"))
        self.player.display(self.screen)
        for cell in self.intense_temperature_cells:
            cell.display(self.screen)

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
