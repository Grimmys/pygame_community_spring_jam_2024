from src.constants import MAIN_WIN_HEIGHT, MAIN_WIN_WIDTH, LIGHT_YELLOW
from src.gui import fonts
from src.scenes.scene import Scene


class GameOver(Scene):

    def __init__(self, screen):
        super().__init__(screen)

    def draw(self):
        super().draw()
        game_over_surface = fonts.fonts["GAME_OVER_FONT"].render("GAME OVER", True,
                                                                 LIGHT_YELLOW)
        self.screen.blit(game_over_surface,
                         (MAIN_WIN_WIDTH // 2 - game_over_surface.get_width() // 2,
                          MAIN_WIN_HEIGHT // 2 - game_over_surface.get_height() // 2))
