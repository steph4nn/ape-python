from pickle import NONE
from random import randint


LINHAS = 2
COLUNAS = 3

matriz_a = [[None]*COLUNAS for i in range(LINHAS)]
matriz_b = [[None]*LINHAS for i in range(COLUNAS)]

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_a[linha][coluna] = randint(1,100)
       

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_b[coluna][linha] = matriz_a[linha][coluna] 


print('Matriz A: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
         print(f'{matriz_a[linha][coluna]:4}',end='')
    print()
 
print('Matriz B: ')
for coluna in range(COLUNAS):
    for linha in range(LINHAS):
         print(f'{matriz_b[coluna][linha]:4}',end='')
    print()
