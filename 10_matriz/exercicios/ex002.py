from random import randint


LINHAS = COLUNAS = 3
matriz_a = [[None]*COLUNAS for i in range(LINHAS)]

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_a[linha][coluna] = randint(1,100)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        if linha == coluna:
            print(f'{matriz_a[linha][coluna]:4}',end='')
    print()
