clothes = ['T-Shirt', 'Sweater']

while True:
    create = input('Welcome! What do you want(C,R,U,D): ')
    create = create.lower()
    
    if create == 'c':
        new_item = input('New item: ')      
        clothes.append(new_item)
        print('Our items: ', end='')
        for i in range(len(clothes)-1):
            print(clothes[i], end=', ')
        print(clothes[len(clothes)-1], end = '')
        print('\n')
        
    elif create == 'r':
        print('Our items:', end=' ')
        for i in range(len(clothes)-1):
            print(clothes[i], end=', ')
        print(clothes[len(clothes)-1])
        print('\n')

    elif create == 'u':
        update_position = int(input('Update position? '))
        new_item = input('New item: ')
        clothes[update_position - 1] = new_item
        print('Our items:', end='')
        for i in range(len(clothes)-1):
            print(clothes[i], end=', ')
        print(clothes[len(clothes)-1])
        print('\n')
        
    elif create == 'd':
        clothes.append('Jeans')
        clothes.append('Jeans')
        remove = int(input('Delete position: '))
        clothes.pop(remove)
        print("Our items:", end=' ')
        for i in range(len(clothes)-1):
            print(clothes[i], end=', ')
        print(clothes[len(clothes)-1])
        print('\n')
        

