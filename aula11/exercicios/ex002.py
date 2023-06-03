frase = input('Digite um frase: ')
frase.split()
tam = len(frase)
for i in range(tam):
    if frase[i] == ' ':
        continue
    else:
        print(frase[i], end='')
