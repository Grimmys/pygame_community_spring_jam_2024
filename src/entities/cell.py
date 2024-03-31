import pygame

from src.gui.position import Position


class Cell:
    DEFAULT_CELL_VELOCITY = 10

    def __init__(
        self, position: Position, size: tuple[int, int], sprite: str | pygame.Surface
    ) -> None:
        self.sprite: pygame.Surface = (
            sprite
            if isinstance(sprite, pygame.Surface)
            else pygame.image.load(sprite).convert_alpha()
        )
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.rect = self.sprite.get_rect()
        self.rect.move_ip(position)
        self.velocity = pygame.Vector2(0, 0)

    def display(self, screen: pygame.Surface) -> None:
        """
        Display the cell on the given screen.

        Keyword arguments:
        screen -- the screen on which the cell should be drawn
        """
        screen.blit(self.sprite, self.rect)

    def update(self, screen: pygame.Surface) -> None:
        self.rect.move_ip(self.velocity)
