#!/usr/bin/env python3

"""
The entry point of the game.
Initiate pygame, load game generic data & fonts, initiate pygame window
and let the main loop running.
The pygame events are caught here and delegated to the start screen.
"""
from pathlib import Path
from os.path import abspath

import pygame
import pygamepopup

from src.constants import GAME_TITLE, MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT, FRAME_RATE
from src.gui import fonts
from src.scenes.main_menu import MainMenu
from src.tools import show_fps


def main_loop(
    screen: pygame.Surface, clock: pygame.time.Clock
) -> None:
    active_scene = MainMenu(screen)
    active_scene.run()

    keep_playing = True
    while keep_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                keep_playing = False
            active_scene.process_event(event)
        screen.fill(pygame.Color("BLACK"))
        active_scene.draw()
        show_fps(screen, clock, fonts.fonts["FPS_FONT"])
        active_scene.update()
        if active_scene.next_scene is not None:
            active_scene.timer_until_next_scene -= 1
            if active_scene.timer_until_next_scene <= 0:
                active_scene = active_scene.next_scene
        elif active_scene.should_stop_game:
            keep_playing = False
        pygame.display.update()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    import platform

    pygame.init()
    pygamepopup.init()

    pygamepopup.configuration.set_info_box_background(
        abspath(Path("assets", "temperature_menu.png"))
    )
    pygamepopup.configuration.set_button_background(abspath(Path("assets", "temperature_menu.png")),
                                                    abspath(Path("assets", "temperature_menu_hover.png")))

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
