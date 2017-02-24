import string
alphabet = list(string.ascii_lowercase)
sentence = input("Your sentence: ")

def count(string, letter):
    count = 0
    for i in string:
        if i.lower() == letter.lower():
            count += 1
    return count
    
for j in alphabet:
    n = count(sentence,j)
    if n>0:
        print("{0} {1}".format(j, n))
