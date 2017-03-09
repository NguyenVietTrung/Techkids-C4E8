class Box:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self, dx, dy):
        return[self.x + dx, self.y + dy]