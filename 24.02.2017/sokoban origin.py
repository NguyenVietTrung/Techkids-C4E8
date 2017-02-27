p = {
    "x": 2,
    "y": 3
} #tao dictionary

boxes = []
boxes.append({"x": 2, "y": 4})
boxes.append({"x": 3, "y": 3})
boxes.append({"x": 1, "y": 1})
boxes.append({"x": 5, "y": 5})

gx = 1
gy = 4

screen_width = 10
screen_height = 10


def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True


def move(x, y, dx, dy):
    return [x + dx, y + dy]

def win_check(bx, by, gx, gy):
    if bx == gx and by == gy:
        print("You win!")
        return True

def print_map(p, boxes, gx, gy, screen_width, screen_height):
    for y in range(screen_height):
        for x in range(screen_width):
            if x == p["x"] and y == p["y"]:
                print("P ", end="")
            elif check_match(boxes, x, y):
                print("B ", end="")
            elif x == gx and y == gy:
                print("G ", end="")
            else:
                print("- ", end="")
        print()
def find_object(objects, x, y):
    for object in objects:
        if object["x"] == x and object["y"] == y:
            return object
    return None

def check_match(objects, x, y):
    for box in objects:
        if box["x"] == x and box["y"] == y:
            return True


    return False #ham nay de y den return sau khi ket thuc vong for

print_map(p, boxes, gx, gy, screen_width, screen_height)

while True:
    print_map(p, boxes, gx, gy, screen_width, screen_height)

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

    [next_px, next_py] = move(p["x"], p["y"], dx, dy)

    if not in_map(next_px, next_py, screen_width, screen_height):
        print("Go away!!!")
    else:
        found_box = find_object(boxes, next_px, next_py)
        if found_box is not None:
            found_box["x"] += dx
            found_box["y"] += dy
            p["x"], p["y"] = next_px, next_py
        else:
            p["x"], p["y"] = next_px, next_py

#         if next_px == bx and next_py == by:
#             [next_bx, next_by] = move(bx, by, dx, dy)
#             if in_map(next_bx, next_by, screen_width, screen_height):
#                 bx, by = next_bx, next_by
#                 p["x"], p["y"] = next_px, next_py
#         else:
#             p["x"], p["y"] = next_px, next_py
#
#     win_check(bx, by, gx, gy)