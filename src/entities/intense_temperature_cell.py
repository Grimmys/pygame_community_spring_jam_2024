from enum import Enum

import pygame

from src.constants import MINIMAL_VERTICAL_GAP_BETWEEN_CELLS, INTENSE_CELL_HORIZONTAL_START, \
    HORIZONTAL_GAP_BETWEEN_CELLS, PERFECT_TEMPERATURE
from src.entities.cell import Cell


class IntenseTemperatureNature(Enum):
    COLD = 1
    WARM = 2
    AMPLIFIER = 3


class IntenseTemperatureCell(Cell):
    DEFAULT_INTENSE_TEMPERATURE_VELOCITY = Cell.DEFAULT_CELL_VELOCITY // 2
    BASE_TEMPERATURE_POWER = 5

    def __init__(
        self, size: tuple[int, int], nature: IntenseTemperatureNature, column_index: int
    ) -> None:
        position = pygame.Vector2(
            INTENSE_CELL_HORIZONTAL_START + (size[0] + HORIZONTAL_GAP_BETWEEN_CELLS) * column_index,
            0)
        match nature:
            case IntenseTemperatureNature.WARM:
                sprite = "assets/warm_cell.png"
            case IntenseTemperatureNature.COLD:
                sprite = "assets/cold_cell.png"
            case IntenseTemperatureNature.AMPLIFIER:
                sprite = "assets/amplifier_cell.png"
            case _:
                raise ValueError(f"{nature} is not a valid intense temperature cell nature")

        super().__init__(position, size, sprite)
        self.velocity.y = IntenseTemperatureCell.DEFAULT_INTENSE_TEMPERATURE_VELOCITY
        self.column_index: int = column_index
        self.nature = nature
        self.alive: bool = True

    def update(self, screen: pygame.Surface) -> None:
        super().update(screen)
        if self.rect.y >= screen.get_height():
            self.alive = False

    def is_position_nearby_spawn(self):
        return self.rect.y < self.rect.size[1] + MINIMAL_VERTICAL_GAP_BETWEEN_CELLS

    def get_temperature_power(self, current_temperature: int) -> int:
        if self.nature is IntenseTemperatureNature.WARM:
            return IntenseTemperatureCell.BASE_TEMPERATURE_POWER
        elif self.nature is IntenseTemperatureNature.COLD:
            return - IntenseTemperatureCell.BASE_TEMPERATURE_POWER
        elif self.nature is IntenseTemperatureNature.AMPLIFIER:
            return IntenseTemperatureCell.BASE_TEMPERATURE_POWER \
                if current_temperature > PERFECT_TEMPERATURE \
                else - IntenseTemperatureCell.BASE_TEMPERATURE_POWER
        return 0
