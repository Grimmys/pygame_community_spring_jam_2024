import pygame

from src.entities.cell import Cell
from src.gui.position import Position


class Player(Cell):
    def __init__(
        self, position: Position, size: tuple[int, int], sprite: str | pygame.Surface
    ) -> None:
        super().__init__(position, size, sprite)
        self.in_movement = False
        self.move_left = False

    def update(self, screen: pygame.Surface):
        self.velocity = pygame.Vector2(0, 0)
        if self.in_movement:
            if self.move_left:
                self.velocity.x -= Cell.DEFAULT_CELL_VELOCITY
            else:
                self.velocity.x += Cell.DEFAULT_CELL_VELOCITY
        super().update(screen)
