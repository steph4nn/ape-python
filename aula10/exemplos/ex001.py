from random import randint


LINHAS = 3
COLUNAS = 3

matriz = [[None]*COLUNAS for i in range(LINHAS)]
print(matriz)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz[linha][coluna] = randint(1,999)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{matriz[linha][coluna]:4}',end='')
    print()

