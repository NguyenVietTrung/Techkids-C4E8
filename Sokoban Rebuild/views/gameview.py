class GameView:
    def __init__(self, image):
        self.image = image
        self.width = 32
        self.height = 32

    def draw(self, screen, game_model):
        x = game_model.x * self.width
        y = game_model.y * self.height
        screen.blit(self.image, (x, y))
