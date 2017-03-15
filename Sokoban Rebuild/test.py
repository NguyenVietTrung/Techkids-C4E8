from models.gamemodel import GameModel

#test 1
game_model = GameModel(2, 3)
game_model.print()

#test 2
game_model.x = 3
game_model.y = 4
game_model.move(1, -1)
assert (game_model.x == 4) and (game_model.y == 3)

#test 3
game_model.x = 4
game_model.y = 5
[next_x, next_y] = game_model.next_pos(1, -2)

assert next_x == 5 and next_y == 3
assert game_model.x == 4 and game_model.y == 5