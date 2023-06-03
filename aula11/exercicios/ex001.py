frase = input('Digite um frase: ')
cont = 0
for i in frase:
    if i == ' ':
        cont+=1
print(cont)