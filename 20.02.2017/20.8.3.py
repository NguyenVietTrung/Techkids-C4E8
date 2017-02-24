##    (a) Python's response: 35
##    (b) Python's response: 4
##    (c) Python's response: True
##    (d) Python's response: Error, pears are not included in d
##    (e) Python's response: 0
##    (f) Python's response: ['apples', 'bananas', 'grapes', 'oranges']
##    (g) Python's response: False

def add_fruit(inventory, fruit, quantity = 0):
    inventory[fruit] = quantity
    return inventory

new_inventory = {}
while True:
    add_fruit(new_inventory, "strawberries", 10)
    if "strawberries" in new_inventory:
        print("True")
    else:
        print("False")
    if new_inventory["strawberries"] == 10:
        print("True")
    else:
        print("False")
        
    add_fruit(new_inventory, "strawberries", 25)
    if new_inventory["strawberries"] == 35:
        print("True")
    else:
        print("False")

