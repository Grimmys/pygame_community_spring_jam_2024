import pygame

from src.constants import MIN_TEMPERATURE, MAX_TEMPERATURE
from src.gui.position import Position


class Thermometer:
    TEMPERATURE_RANGE = MAX_TEMPERATURE - MIN_TEMPERATURE

    def __init__(self, position: Position):
        self.position = position
        self.base_sprite = pygame.image.load("assets/thermometer.png")
        self.fill_sprite = pygame.image.load("assets/thermometer_filled.png")

    def display(self, screen: pygame.Surface, temperature: int) -> None:
        screen.blit(self.base_sprite, self.position)
        fill_proportion = temperature / Thermometer.TEMPERATURE_RANGE
        fill_rect = self.fill_sprite.get_rect()
        fill_rect.y = fill_rect.height * (1 - fill_proportion)
        screen.blit(self.fill_sprite, self.position + pygame.Vector2(0, fill_rect.y), fill_rect)

