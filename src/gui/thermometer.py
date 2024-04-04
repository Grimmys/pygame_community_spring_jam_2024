from pathlib import Path

import pygame

from src.constants import MIN_TEMPERATURE, MAX_TEMPERATURE, WARNING_SIGN_SIZE
from src.gui.position import Position


class Thermometer:
    TEMPERATURE_RANGE = MAX_TEMPERATURE - MIN_TEMPERATURE
    TOP_MARGIN = 10
    LOW_TEMPERATURE_LIMIT = 0.2
    HIGH_TEMPERATURE_LIMIT = 0.8

    def __init__(self, position: Position):
        self.position = position
        self.base_sprite = pygame.image.load(Path("assets", "thermometer.png"))
        self.temperature_level_sprite = pygame.image.load(Path("assets", "temperature_surface.png"))
        self.fill_sprite = pygame.image.load(Path("assets", "thermometer_filled.png"))
        self.warning_sign = pygame.transform.scale(pygame.image.load(Path("assets", "warning.png")), WARNING_SIGN_SIZE)

    def display(self, screen: pygame.Surface, temperature: int) -> None:
        screen.blit(self.base_sprite, self.position)
        fill_proportion = temperature / Thermometer.TEMPERATURE_RANGE
        fill_rect = self.fill_sprite.get_rect()
        fill_rect.y = fill_rect.height * (1 - fill_proportion)
        screen.blit(self.fill_sprite, self.position + pygame.Vector2(0, fill_rect.y), fill_rect)
        if 0.1 <= fill_proportion <= 0.9:
            screen.blit(self.temperature_level_sprite, self.position +
                        pygame.Vector2(0, fill_rect.y - self.temperature_level_sprite.get_height()))
        if (Thermometer.LOW_TEMPERATURE_LIMIT >= fill_proportion or
                fill_proportion >= Thermometer.HIGH_TEMPERATURE_LIMIT):
            screen.blit(self.warning_sign, self.position +
                        pygame.Vector2(self.base_sprite.get_width() // 2 - self.warning_sign.get_width() // 2,
                                       - self.warning_sign.get_height() - Thermometer.TOP_MARGIN))
