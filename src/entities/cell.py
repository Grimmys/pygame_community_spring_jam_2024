import pygame

from src.gui.position import Position


class Cell:
    def __init__(
        self, position: Position, size: tuple[int, int], sprite: str | pygame.Surface
    ) -> None:
        self.position: Position = position
        self.sprite: pygame.Surface = (
            sprite
            if isinstance(sprite, pygame.Surface)
            else pygame.image.load(sprite).convert_alpha()
        )
        self.sprite = pygame.transform.scale(self.sprite, size)

    def display(self, screen: pygame.Surface) -> None:
        """
        Display the cell on the given screen.

        Keyword arguments:
        screen -- the screen on which the cell should be drawn
        """
        screen.blit(self.sprite, self.position)
