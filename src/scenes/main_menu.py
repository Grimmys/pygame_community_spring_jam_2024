from os.path import abspath
from pathlib import Path

import pygame
from pygamepopup.components import InfoBox, Button, TextElement, ImageButton
from pygamepopup.menu_manager import MenuManager

from src.constants import NEW_GAME_TEXT, GAME_TITLE, EXIT_GAME_TEXT, MAIN_MENU_WIDTH, \
    HIGH_SCORE_TEXT, HIGH_SCORE_MENU_WIDTH, RED, CRYSTAL_WHITE, BLUE, HELP_TEXT, \
    HELP_MENU_WIDTH, GLOSSARY_TEXT, GLOSSARY_MENU_WIDTH, CONTROLS_TEXT, CONTROLS_MENU_WIDTH
from src.gui import fonts
from src.scenes.game import Game
from src.scenes.scene import Scene
from src.tools import load_high_scores


class MainMenu(Scene):

    def __init__(self, screen):
        super().__init__(screen)

        self.menu_manager = MenuManager(screen)
        self.menu_manager.open_menu(InfoBox(
            GAME_TITLE,
            [
                [
                    Button(title=NEW_GAME_TEXT, callback=self.new_game),
                ],
                [
                    Button(title=HELP_TEXT, callback=self.see_help)
                ],
                [
                    Button(title=HIGH_SCORE_TEXT, callback=self.see_high_score)
                ],
                [
                    Button(title=EXIT_GAME_TEXT, callback=self.exit_game)
                ],
            ],
            width=MAIN_MENU_WIDTH,
            has_close_button=False,
        ))

    def draw(self):
        super().draw()
        self.menu_manager.display()

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.menu_manager.motion(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.menu_manager.click(event.button, event.pos)

    def new_game(self):
        self.next_scene = Game(self.screen)

    def see_high_score(self):
        high_scores = load_high_scores()
        self.menu_manager.open_menu(InfoBox(
            HIGH_SCORE_TEXT,
            [
                [
                    TextElement(text=f"1 — {high_scores[0]}", text_color=RED,
                                font=fonts.fonts["HIGH_SCORE_FONT"]),
                ],
                [
                    TextElement(text=f"2 — {high_scores[1]}", text_color=CRYSTAL_WHITE,
                                font=fonts.fonts["HIGH_SCORE_FONT"])
                ],
                [
                    TextElement(text=f"3 — {high_scores[2]}", text_color=BLUE,
                                font=fonts.fonts["HIGH_SCORE_FONT"]),
                ],
            ],
            width=HIGH_SCORE_MENU_WIDTH,
            has_close_button=True,
        ))

    def see_help(self):
        self.menu_manager.open_menu(InfoBox(
            HELP_TEXT,
            [
                [
                    TextElement(text="As a fragile temperate cell, you need to take care of cells with intense "
                                     "temperature which can threaten your life.")
                ],
                [
                    TextElement(text="Diverge too much from the perfect temperature, and this will be the end of your "
                                     "petty existence.")
                ],
                [
                    TextElement(text="So make sure to avoid all these cells that will keep swarming you.")
                ],
                [
                    Button(title=GLOSSARY_TEXT, callback=self.see_glossary, margin=(10, 0, 0, 0)),
                    Button(title=CONTROLS_TEXT, callback=self.see_controls, margin=(10, 0, 0, 0))
                ],
            ],
            width=HELP_MENU_WIDTH,
            has_close_button=True,
        ))

    def see_glossary(self):
        self.menu_manager.open_menu(InfoBox(
            GLOSSARY_TEXT,
            [
                [
                    ImageButton(image_path=abspath(Path("assets", "cold_cell.png")), size=(64, 64),
                                background_path=abspath(Path("assets", "empty.png")), frame_background_path=abspath(Path("assets",  "empty.png")), frame_background_hover_path=abspath(Path("assets",  "empty.png"))),
                    TextElement(text="Cold Cell: its temperature is quite low. Hitting it will make you colder.", column_span=3)
                ],
                [
                    ImageButton(image_path=abspath(Path("assets", "warm_cell.png")), size=(64, 64),
                                background_path=abspath(Path("assets", "empty.png")), frame_background_path=abspath(Path("assets",  "empty.png")), frame_background_hover_path=abspath(Path("assets",  "empty.png"))),
                    TextElement(text="Warm Cell: its temperature is quite high. Hitting it will make you warmer.", column_span=3)
                ],
                [
                    ImageButton(image_path=abspath(Path("assets", "amplifier_cell.png")), size=(64, 64),
                                background_path=abspath(Path("assets", "empty.png")), frame_background_path=abspath(Path("assets",  "empty.png")), frame_background_hover_path=abspath(Path("assets",  "empty.png"))),
                    TextElement(text="Amplifier Cell: its weird consistence will amplify your current gap from "
                                     "perfect temperature. Avoid them at all cost.", column_span=3)
                ],
            ],
            width=GLOSSARY_MENU_WIDTH,
            has_close_button=True,
        ))

    def see_controls(self):
        self.menu_manager.open_menu(InfoBox(
            CONTROLS_TEXT,
            [
                [
                    TextElement(text="Move left:"),
                    TextElement(text="S or left arrow",
                                column_span=2)
                ],
                [
                    TextElement(text="Move right:"),
                    TextElement(text="F or right arrow",
                                column_span=2)
                ],
            ],
            width=CONTROLS_MENU_WIDTH,
            has_close_button=True,
        ))

    def exit_game(self):
        self.should_stop_game = True
