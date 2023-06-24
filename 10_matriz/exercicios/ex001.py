from random import randint


LINHAS = 2
COLUNAS = 3

matriz_a = [[None]*COLUNAS for i in range(LINHAS)]
matriz_b = [[None]*COLUNAS for i in range(LINHAS)]
matriz_c = [[None]*COLUNAS for i in range(LINHAS)]

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_a[linha][coluna] = randint(1,99)
    
#MATRIZ A GERADA

print('Matriz A: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
         print(f'{matriz_a[linha][coluna]:4}',end='')
    print()


for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_b[linha][coluna] = randint(1,100)

#MATRIZ B GERADA 

print('Matriz B: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
         print(f'{matriz_b[linha][coluna]:4}',end='')
    print()


for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_c[linha][coluna] = matriz_a[linha][coluna] + matriz_b[linha][coluna]

#MATRIZ C GERADA 
print('Matriz C: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
         print(f'{matriz_c[linha][coluna]:4}',end='')
    print()