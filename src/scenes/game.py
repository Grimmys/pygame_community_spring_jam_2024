import random
from typing import Optional

import pygame

from src.constants import PLAYER_INITIAL_POSITION, PLAYER_SIZE, INTENSE_TEMPERATURE_CELL_SIZE, \
    HORIZONTAL_GAP_BETWEEN_CELLS, MINIMAL_VERTICAL_GAP_BETWEEN_CELLS, INTENSE_CELL_HORIZONTAL_START
from src.entities.cell import Cell
from src.entities.player import Player
from src.scenes.scene import Scene


class Game(Scene):
    INTENSE_CELL_COLUMNS_NUMBER = 6

    def __init__(self, screen):
        super().__init__(screen)
        self.player: Player = Player(pygame.Vector2(PLAYER_INITIAL_POSITION), PLAYER_SIZE,
                                     "assets/player_cell.png")
        self.intense_temperature_cells = []
        for _ in range(3):
            cell: Optional[Cell] = self._generate_intense_temperature_cell()
            if cell:
                self.intense_temperature_cells.append(cell)
        self.double_movement_key_pressed: bool = False

    def _generate_intense_temperature_cell(self) -> Optional[Cell]:
        free_columns = list(range(Game.INTENSE_CELL_COLUMNS_NUMBER))
        for cell in self.intense_temperature_cells:
            cell_column = (cell.rect.x - INTENSE_CELL_HORIZONTAL_START) // (
                INTENSE_TEMPERATURE_CELL_SIZE[0] + HORIZONTAL_GAP_BETWEEN_CELLS)
            if (cell_column in free_columns and
                cell.rect.y < INTENSE_TEMPERATURE_CELL_SIZE[1] +
                MINIMAL_VERTICAL_GAP_BETWEEN_CELLS):
                free_columns.remove(cell_column)

        if len(free_columns) == 0:
            return None

        column_index = random.choice(free_columns)
        return Cell(pygame.Vector2(INTENSE_CELL_HORIZONTAL_START + (
            INTENSE_TEMPERATURE_CELL_SIZE[0] + HORIZONTAL_GAP_BETWEEN_CELLS) * column_index, 0),
                    INTENSE_TEMPERATURE_CELL_SIZE,
                    "assets/cold_cell.png")

    def update(self):
        super().update()
        self.player.update()

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
