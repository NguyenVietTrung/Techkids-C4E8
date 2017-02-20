shipsizes = [5, 10, 15, 20, 25, 30, 100]

print('Hello, my name is Trung and these are my ship sizes: ', '')
print(shipsizes)

print ('Now my biggest sheep has size', max(shipsizes), "let's shear it")

shipsizes[shipsizes.index(max(shipsizes))] = 8
print('After shearing, here is my flock:', '\n',shipsizes)
