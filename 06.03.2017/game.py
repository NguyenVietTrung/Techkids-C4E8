import pygame
from box import Box
from gate import Gate

pygame.init()
screen = pygame.display.set_mode([200, 200])

COLOR_WHITE = (255, 255, 255)
player_image = pygame.image.load("roshan.png")
square_image = pygame.image.load("square.png")
box_image = pygame.image.load("shield.jpg")
gate_iamge = pygame.image.load("gate.png")
win_image = pygame.image.load("youwin.png")

x, y = 100, 100
SQUARE_SIZE = 32

class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self, dx, dy):
        return[self.x + dx, self.y + dy]

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(0, 0)
        self.box = Box(4, 4)
        self.gate = Gate(0, 5)

    def check_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def move_objects(self, dx, dy):
        [next_player_x, next_player_y] = self.player.calc_next_position(dx, dy)
        [next_box_x, next_box_y] = self.box.calc_next_position(dx, dy)
        if not self.check_inside(next_player_x, next_player_y):
            None
        elif [next_player_x, next_player_y] == [self.box.x, self.box.y]:
            if self.check_inside(next_box_x, next_box_y):
                self.player.move(dx, dy)
                self.box.move(dx, dy)
        else:
            self.sound_once("Pickup_Coin.wav")
            self.player.move(dx, dy)

    def sound_once(self, file_name):
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play(0)

    def check_win(self):
        if [self.box.x, self.box.y] == [self.gate.x, self.gate.y]:
            done = True
            return done

done = False
map = Map(6, 6)

while not done:
    key_arrow = None

    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1

    #Process game events
    if dx != 0 or dy != 0:
        print(dx, dy)
        map.move_objects(dx, dy)

    #Repaint
    screen.fill(COLOR_WHITE)
    for y in range(map.height):
        for x in range(map.width):
          screen.blit(square_image, (x*SQUARE_SIZE, y*SQUARE_SIZE))
          screen.blit(gate_iamge, (map.gate.x * SQUARE_SIZE, map.gate.y * SQUARE_SIZE))
    screen.blit(box_image, (map.box.x*SQUARE_SIZE, map.box.y*SQUARE_SIZE))
    screen.blit(player_image, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))
    if map.check_win():
        screen.blit(win_image, (0, 0))

    pygame.display.flip()