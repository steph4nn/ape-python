from random import randint


N = int(input('Digite a ordem da matriz: '))
LINHAS = COLUNAS = N

matriz_a = [[None]*COLUNAS for i in range(LINHAS)]
matriz_b = [[None]*COLUNAS for i in range(LINHAS)]

#gerando matriz A
for linha in  range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_a[linha][coluna] = randint(1,100)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        if linha == coluna:
            matriz_b[linha][coluna] = 0
        elif coluna +linha == N-1:
            matriz_b[linha][coluna] = 0
        else:
            matriz_b[linha][coluna] = matriz_a[linha][coluna] + linha + coluna

print('Matriz A: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
         print(f'{matriz_a[linha][coluna]:4}',end='')
    print()
 
print('Matriz B: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
         print(f'{matriz_b[linha][coluna]:4}',end='')
    print()

