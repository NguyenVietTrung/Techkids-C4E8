##alphabet = list(string.ascii_lowercase)
##sentence = input("Your sentence: ")
##
##for i in range(len(sentence)):
##    if sentence[i] in alphabet:

a = input("Nhap vao nhanh: ")
d = {}
for i in range(len(a)):
    if(a[i] not in d.keys()):
       d[a[i]] = 1
    else:
        d[a[i]] = d[a[i]] + 1
for key, value in sorted(d.items()):
       if(value > 0):
           print(key + "\t" , value)
