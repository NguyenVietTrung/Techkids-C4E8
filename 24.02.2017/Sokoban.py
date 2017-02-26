px = 1
py = 2
bx = 2
by = 2
cx = 4
cy = 3

screen_width = 5
screen_height = 5


def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True

def move(x, y, dx, dy):
    return [x + dx, y + dy]

def win_check(bx, by, cx, cy):
    if bx == cx and by == cy:
        print("You win!")
        return False
    return True

def box_in_corner(bx, by):
    if bx == 0 and by == 0:
        print("You lose!")
        return False
    elif bx == 0 and by == screen_height - 1:
        print("You lose!")
        return False
    elif bx == screen_width and by == 0:
        print("You lose!")
        return False
    elif bx == screen_width - 1 and by == screen_height - 1:
        print("You lose!")
        return False
    else:
        return True

def touch_box(px, py, bx, by):
    if px - bx == 0 and py - by == -1:
        print("You've touched the box")
        return True
    if px - bx == 0 and by - py == -1:
        print("You've touched the box")
        return True
    if py - by == 0 and bx - px == -1:
        print("You've touched the box")
        return True
    if py - by == 0 and bx - px == -1:
        print("You've touched the box")
        return True
while True:
    for y in range(screen_height):
        for x in range(screen_width):
            if x == px and y == py:
                print("P ", end="")
            elif x == bx and y == by:
                print("B ", end="")
            elif x == cx and y == cy:
                print("o", end="")
            else:
                print("- ", end="")
        print()

    choice = input("What do you want? U - D - L - R: ").upper()

    dx = 0
    dy = 0

    if choice == "W":
        dy = -1
    elif choice == "S":
        dy = 1
    elif choice == "A":
        dx = -1
    elif choice == "D":
        dx = 1

    [next_px, next_py] = move(px, py, dx, dy)
    [next_bx, next_by] = move(bx, by, dx, dy)

    if not in_map(next_px, next_py, screen_width, screen_height):
        print("Go away!!!")
    else:
        px = next_px
        py = next_py
        bx = next_bx
        by = next_by
    win_check(bx, by, cx, cy)
    box_in_corner(bx, by)
    touch_box(px, py, bx, by)

