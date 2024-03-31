import pygame

from src.constants import MINIMAL_VERTICAL_GAP_BETWEEN_CELLS, INTENSE_CELL_HORIZONTAL_START, \
    HORIZONTAL_GAP_BETWEEN_CELLS
from src.entities.cell import Cell


class IntenseTemperatureCell(Cell):
    DEFAULT_INTENSE_TEMPERATURE_VELOCITY = Cell.DEFAULT_CELL_VELOCITY // 2

    def __init__(
        self, size: tuple[int, int], sprite: str | pygame.Surface, column_index: int
    ) -> None:
        position = pygame.Vector2(
            INTENSE_CELL_HORIZONTAL_START + (size[0] + HORIZONTAL_GAP_BETWEEN_CELLS) * column_index,
            0)
        super().__init__(position, size, sprite)
        self.velocity.y = IntenseTemperatureCell.DEFAULT_INTENSE_TEMPERATURE_VELOCITY
        self.column_index = column_index

    def is_position_nearby_spawn(self):
        return self.rect.y < self.rect.size[1] + MINIMAL_VERTICAL_GAP_BETWEEN_CELLS
