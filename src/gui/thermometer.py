import pygame

from src.gui.position import Position


class Thermometer:

    def __init__(self, position: Position):
        self.position = position
        self.base_sprite = pygame.image.load("assets/thermometer.png")
        self.fill_sprite = pygame.image.load("assets/thermometer_filled.png")
        self.fill_proportion = 0.5

    def display(self, screen: pygame.Surface) -> None:
        screen.blit(self.base_sprite, self.position)
        fill_rect = self.fill_sprite.get_rect()
        fill_rect.y = fill_rect.height * self.fill_proportion
        screen.blit(self.fill_sprite, self.position + pygame.Vector2(0, fill_rect.y), fill_rect)

