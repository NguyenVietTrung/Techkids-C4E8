from player import Player

class Map:
    def __init__(self, width, height):
        self.player = Player(2, 2)
        self.width = width
        self.height = height
    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.player.match(x, y):
                    print(self.player.text, end="")
                else:
                    print("- ", end="")
            print()

    def move_player(self, dx, dy):
        self.player.move(dx, dy)

    def process_input(self, move): #A,S,D,W
        direction = move.upper()
        dx, dy = 0, 0
        if direction == "W":
            dx, dy = 0, -1
        elif direction == "S":
            dx, dy = 0, 1
        elif direction == "A":
            dx, dy = -1, 0
        elif direction == "D":
            dx, dy = 1, 0

        self.move_player(dx, dy)

    def loop(self):
        while True:
            self.print()
            move = input("Your move (A,S,D,W): ")
            self.process_input(move)

map = Map(7,7)
map.loop()