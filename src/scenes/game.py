import pygame

from src.constants import PLAYER_INITIAL_POSITION, PLAYER_SIZE
from src.entities.cell import Cell
from src.scenes.scene import Scene


class Game(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.player = Cell(pygame.Vector2(PLAYER_INITIAL_POSITION), PLAYER_SIZE, "assets/player_cell.png")

    def draw(self):
        super().draw()
        self.screen.fill(pygame.Color("BLACK"))
        self.player.display(self.screen)
