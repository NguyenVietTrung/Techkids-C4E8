class Player:
    def __init__(self, x, y):  #constructor
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x, self.y = x,y

    def calc_next(self, dx, dy):
        return [self.x + dx, self.y + dy] #tra ve gia tri tam thoi

    def match(self, x, y):
        if self.x == x and self.y == y:
            self.text = "P "
            return True
#player = Player(1,2 )  # tuc la player.x = 3, player.y = 2