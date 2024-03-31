"""
Defines fonts that will be used all over the application.
The init_fonts function should be called at the beginning of the application
after pygame initialization.
"""
import pygame

_fonts_description: dict[str, dict[str, str | int]] = {
    "FPS_FONT": {"default": True, "size": 20},
    "GAME_OVER_FONT": {"default": True, "size": 64}
}

fonts: dict[str, pygame.font.Font] = {}


def init_fonts() -> None:
    """
    Load all fonts registered in fonts_description.
    System font will be load if the keyword 'default' is present in the description provided.
    These fonts will be available in all modules by importing fonts dictionary.
    """
    for font_name, font in _fonts_description.items():
        if "default" in font:
            # Use pygame's default font
            fonts[font_name] = pygame.font.SysFont("arial", font["size"], True)
        else:
            fonts[font_name] = pygame.font.Font(font["name"], font["size"])
