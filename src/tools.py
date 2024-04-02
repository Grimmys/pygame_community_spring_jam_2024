import pickle

import pygame

from src.constants import LIGHT_YELLOW


def show_fps(
    surface: pygame.Surface, inner_clock: pygame.time.Clock, font: pygame.font.Font
) -> None:
    """
    Display in the top left corner of the screen the current frame rate.

    Keyword arguments:
    screen -- the surface on which the framerate should be drawn
    inner_clock -- the pygame clock running and containing the current frame rate
    font -- the font used to display the frame rate
    """
    fps_text = font.render(f"FPS: {inner_clock.get_fps():.0f}", True, LIGHT_YELLOW)
    surface.blit(fps_text, (2, 2))


def load_high_scores() -> list[int]:
    try:
        with open("high_scores.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return [0, 0, 0]
