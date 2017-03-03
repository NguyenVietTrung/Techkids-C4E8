p = {}
p["x"] = 2
p["y"] = 3

screen_width = 12
screen_height = 12
gates = []
gates.append({"x" : 3, "y" :7})
gates.append({"x" : 4, "y" :8})
gates.append({"x" : 5, "y" :9})
boxes = []
boxes.append({"x" : 5,"y" : 5})
boxes.append({"x" : 5,"y" : 8})
boxes.append({"x" : 5,"y" : 6})

def check_match(object, x, y):
    for box in object:
        if box["x"] == x and box["y"] == y:
            return True
    return False

def find_objects(objects, x, y):
    for object in objects:
        if object["x"] == x and object["y"] == y:
            return object
    return None

def print_map(boxes, p, gates, screen_width, screen_height):
    for y in range(screen_height):
        for x in range(screen_width):
            if x == p["x"] and y == p["y"]:
                print("P", end=" ")
            elif check_match(boxes, x, y):
                print("B", end=" ")
            elif check_match(gates, x, y):
                print("*", end=" ")
            else:
                print("-", end=" ")
        print()

def check_win(boxes, gates):
    for i in range(len(boxes)):
        if(boxes[i]["x"] != gates[i]["x"]) or (boxes[i]["y"] != gates[i]["y"]):
            return False
    return True

def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True

def move(x, y, dx, dy):
    return [x + dx, y + dy]

while True:
    print_map(boxes, p, gates, screen_width, screen_height)
    choice = input("what do you want? : ").upper()

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
        print("go away!!!")
    else:
        found_box = find_objects(boxes, next_px, next_py)
        if found_box is not None:
            next_bx = found_box["x"] + dx
            next_by = found_box["y"] + dy
            if not check_match(boxes, next_bx, next_by) and in_map(next_bx, next_by, screen_width, screen_height):
                found_box["x"] += dx
                found_box["y"] += dy
                p["x"], p["y"] = next_px, next_py
        else:
            p["x"], p["y"] = next_px, next_py
    if check_win(boxes, gates):
        print("YOU WIN")
        break