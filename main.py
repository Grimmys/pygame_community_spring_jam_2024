#!/usr/bin/env python3

"""
The entry point of the game.
Initiate pygame, load game generic data & fonts, initiate pygame window
and let the main loop running.
The pygame events are caught here and delegated to the start screen.
"""

import pygame

from src.constants import GAME_TITLE, MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT, FRAME_RATE
from src.gui import fonts
from src.scenes.game import Game
from src.tools import show_fps


def main_loop(
    screen: pygame.Surface, clock: pygame.time.Clock
) -> None:
    active_scene = Game(screen)
    active_scene.run()

    keep_playing = True
    while keep_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                keep_playing = False
            active_scene.process_event(event)
        active_scene.draw()
        show_fps(screen, clock, fonts.fonts["FPS_FONT"])
        active_scene.update()
        pygame.display.update()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    import platform

    pygame.init()

    fonts.init_fonts()

    pygame.display.set_caption(GAME_TITLE)
    main_screen = pygame.display.set_mode((MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT))

    # Make sure the game will display correctly on high DPI monitors on Windows.
    if platform.system() == "Windows":
        from ctypes import windll

        try:
            windll.user32.SetProcessDPIAware()
        except AttributeError:
            pass

    # Let's start the game!
    main_loop(main_screen, pygame.time.Clock())

    pygame.quit()
