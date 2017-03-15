from models.gamemodel import GameModel
from views.gameview import GameView
import pygame

class PlayerController:
    def __init__(self, game_model, game_view):
        self.game_model = game_model
        self.game_view = game_view

    def draw(self, screen):
        self.game_view.draw(screen, self.game_model)

    def process_input(self, key):
        if key == pygame.K_DOWN:
            self.game_model.move(0 ,1)
        elif key == pygame.K_UP:
            self.game_model.move(0, -1)
        elif key == pygame.K_LEFT:
            self.game_model.move(-1 ,0)
        elif key == pygame.K_RIGHT:
            self.game_model.move(1, 0)

#factory
def create_player(x, y):
    game_model = GameModel(x, y)
    game_view = GameView(pygame.image.load("images/mario-1.png"))
    return PlayerController(game_model, game_view)
