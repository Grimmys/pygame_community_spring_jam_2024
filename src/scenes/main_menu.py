import pygame
from pygamepopup.components import InfoBox, Button, TextElement
from pygamepopup.menu_manager import MenuManager

from src.constants import NEW_GAME_TEXT, GAME_TITLE, EXIT_GAME_TEXT, MAIN_MENU_WIDTH, \
    HIGH_SCORE_TEXT, HIGH_SCORE_MENU_WIDTH, RED, CRYSTAL_WHITE, BLUE, BLACK, HELP_TEXT, HELP_TEXT_MENU_WIDTH
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
                    Button(title=NEW_GAME_TEXT, callback=self.new_game, text_hover_color=BLACK),
                ],
                [
                    Button(title=HELP_TEXT, callback=self.see_help, text_hover_color=BLACK)
                ],
                [
                    Button(title=HIGH_SCORE_TEXT, callback=self.see_high_score, text_hover_color=BLACK)
                ],
                [
                    Button(title=EXIT_GAME_TEXT, callback=self.exit_game, text_hover_color=BLACK),
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
            ],
            width=HELP_TEXT_MENU_WIDTH,
            has_close_button=True,
        ))

    def exit_game(self):
        self.should_stop_game = True
