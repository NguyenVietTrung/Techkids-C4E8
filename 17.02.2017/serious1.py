clothes = ["T-Shirt", "Sweater"]

while True:
    create = input("Welcome. What do you want(C,R,U,D): ")
    create = create.lower()
    
    if create =="c":
        add = input("New item: ")      
        clothes.append(add)
        print("Our items: ", end=' ')
        for i in range(len(clothes-1)):
            print(clothes[i], end=', ')
        print(clothes[(len(clothes))-1])
        print()
    else:
        print()
        
##    elif (a=="r"):
##        print("Our items:", end=' ')
##        for i in range(len(clothes)-1):
##            print(clothes[i], end=', ')
##        print(clothes[len(clothes)-1])
##    elif (a=="d"):
##        position = int(input("Delete position? "))
##        clothe.pop(position)
##        print("Our items:", end=' ')
##        for i in range(len(clothe)-1):
##            print(clothe[i], end=', ')
##        print(clothe[len(clothe)-1])
##    elif (a=="u"):
##        position = int(input("Update position? "))
##        new_clothe = input("New item? ")
##        clothe[position] = new_clothe
##        print("Our items:", end=' ')
##        for i in range(len(clothe)-1):
##            print(clothe[i], end=', ')
##        print(clothe[len(clothe)-1])
##    print()
