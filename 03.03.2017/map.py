from player import Player
from box import Box
from gate import Gate

class Map:
    def __init__(self, width, height):
        self.player = Player(2,2)
        self.box = Box(3,3)
        self.gate = Gate(4,4)
        self.width = width
        self.height = height

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.player.match(x, y):
                    print(self.player.text, end="")
                elif self.box.match(x, y):
                    print(self.box.text, end="")
                elif self.gate.match(x, y):
                    print(self.gate.text, end="")
                else:
                    print("- ", end="")
            print()

    def move_player(self, dx, dy):
        self.player.move(dx, dy)

    def move_box(self, dx, dy):
        self.box.move(dx, dy)

    def in_map(self, x, y):
        if x < 0 or y < 0 or x > self.width - 1 or y > self.height - 1:
            return True
        return False

    def process_input(self, move):
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

        next_px, next_py = self.player.calc_next(dx, dy)
        if self.in_map(next_px, next_py):
            print("Another direction please! ")
        else:
            next_bx, next_by = self.box.x + dx, self.box.y + dy
            if next_px == self.box.x and next_py == self.box.y:
                if self.in_map(next_bx, next_by):
                    print("Your box is facing wall, another direction please!")
                else:
                    self.player.move(dx, dy)
                    self.box.move(dx, dy)
            else:
                self.player.move(dx, dy)

    def loop(self):
        while True:
            self.print()
            move = input("Your move (A,S,D,W): ")
            self.process_input(move)
            if self.box.x == self.gate.x and self.box.y == self.gate.y:
                print("You win the game, congrats!")
                self.print()
                break

map = Map(7,7)
map.loop()