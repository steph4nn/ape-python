frase = input('Digite um frase: ')
tam = len(frase)
print(frase)
print(frase[::-1])


for i in range(tam):
    if frase[i] == frase[::-1][i]:
        print('é palíndromo')
    else:
        print('Não é.')