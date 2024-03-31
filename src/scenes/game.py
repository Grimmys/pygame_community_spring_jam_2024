import pygame

from src.constants import PLAYER_INITIAL_POSITION, PLAYER_SIZE
from src.entities.player import Player
from src.scenes.scene import Scene


class Game(Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.player: Player = Player(pygame.Vector2(PLAYER_INITIAL_POSITION), PLAYER_SIZE,
                                     "assets/player_cell.png")
        self.double_movement_key_pressed = False

    def update(self):
        super().update()
        self.player.update()

    def draw(self):
        super().draw()
        self.screen.fill(pygame.Color("BLACK"))
        self.player.display(self.screen)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_f:
                if self.player.in_movement:
                    self.double_movement_key_pressed = True
                else:
                    self.player.in_movement = True
                self.player.move_left = event.key == pygame.K_s
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_f:
                if self.double_movement_key_pressed:
                    self.double_movement_key_pressed = False
                else:
                    self.player.in_movement = False
