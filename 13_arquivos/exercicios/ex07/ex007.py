file = open('conca.txt','r')
list = file.read()

cont = 0
for word in list:
    for letter in word:
        cont+=1
print(cont)

file.close()