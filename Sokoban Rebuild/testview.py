import pygame

from models.gamemodel import GameModel
from views.gameview import GameView

pygame.init()
pygame.display.set_caption("Introduction to pygame")
screen = pygame.display.set_mode((400, 300))
done = False
BACK_GROUND = (148, 198, 153)

game_model = GameModel(2, 3)
game_view = GameView(pygame.image.load("images/mario-1.png"))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BACK_GROUND)
    game_view.draw(screen, game_model)
    pygame.display.flip()