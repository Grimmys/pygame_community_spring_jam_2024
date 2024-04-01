import pygame
from pygame import Event
from pygamepopup.components import InfoBox, Button
from pygamepopup.menu_manager import MenuManager

from src.constants import NEW_GAME_TEXT, GAME_TITLE, EXIT_GAME_TEXT, MAIN_MENU_WIDTH
from src.scenes.game import Game
from src.scenes.scene import Scene


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
                    Button(title=EXIT_GAME_TEXT, callback=self.exit_game),
                ],
            ],
            width=MAIN_MENU_WIDTH,
            has_close_button=False,
        ))

    def draw(self):
        super().draw()
        self.menu_manager.display()

    def process_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.menu_manager.motion(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.menu_manager.click(event.button, event.pos)

    def new_game(self):
        self.next_scene = Game(self.screen)

    def exit_game(self):
        self.should_stop_game = True
