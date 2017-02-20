shipsizes = [5, 10, 15, 20, 25, 30, 100]

print('Hello, my name is Trung and these are my ship sizes: ', '')
print(shipsizes)

for j in range(1,5):
    print ('Now my biggest sheep has size', max(shipsizes), "let's shear it")
    shipsizes[shipsizes.index(max(shipsizes))] = 8
    print('After shearing, here is my flock:', '\n',shipsizes)   
    print('MONTH', j,':')
    for i in range(len(shipsizes)):
        shipsizes[i-1] = int(shipsizes[i-1])+50
    print('One month has passed, now here is my flock:','\n',shipsizes)
print()
