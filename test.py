from random import randint

ordem = int(input('Digite a ordem da matriz: '))
matriz = [[None]*ordem for i in range(ordem)]

for linha in range(ordem):
    for coluna in range(ordem):
        matriz[linha][coluna] = randint(1,10)

for linha in range(ordem):
    for coluna in range(ordem):
        print(f'{matriz[linha][coluna]:4}', end='')
    print('')