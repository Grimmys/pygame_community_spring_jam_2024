import pygame

from src.constants import MAIN_WIN_HEIGHT, MAIN_WIN_WIDTH, LIGHT_YELLOW, GAME_OVER_TEXT, SCORE_TEXT, \
    DIFFICULTY_LEVEL_TEXT
from src.gui import fonts
from src.scenes.scene import Scene


class GameOver(Scene):

    def __init__(self, screen, score: int, difficulty_level: int):
        super().__init__(screen)
        self.score = score
        self.difficulty_level = difficulty_level

    def draw(self):
        super().draw()
        game_over_surface = fonts.fonts["GAME_OVER_FONT"].render(GAME_OVER_TEXT, True,
                                                                 LIGHT_YELLOW)
        self.screen.blit(game_over_surface,
                         (MAIN_WIN_WIDTH // 2 - game_over_surface.get_width() // 2,
                          MAIN_WIN_HEIGHT // 3 - game_over_surface.get_height() // 2))

        game_over_score = fonts.fonts["GAME_OVER_STATS_FONT"].render(f"{SCORE_TEXT}: {self.score}",
                                                                     True, LIGHT_YELLOW)
        self.screen.blit(game_over_score,
                         (MAIN_WIN_WIDTH // 2 - game_over_score.get_width() // 2,
                          3 * MAIN_WIN_HEIGHT // 4 - game_over_score.get_height() // 2)
                         )

        game_over_difficulty_level = fonts.fonts["GAME_OVER_STATS_FONT"].render(f"{DIFFICULTY_LEVEL_TEXT}: {self.difficulty_level}", True, LIGHT_YELLOW)
        self.screen.blit(game_over_difficulty_level,
                         (MAIN_WIN_WIDTH // 2 - game_over_difficulty_level.get_width() // 2,
                          3 * MAIN_WIN_HEIGHT // 4 - game_over_difficulty_level.get_height() // 2 + game_over_score.get_height())
                         )

    def process_event(self, event: pygame.event.Event) -> None:
        from src.scenes.main_menu import MainMenu
        if event.type == pygame.MOUSEBUTTONUP:
            self.next_scene = MainMenu(self.screen)
