from random import randint
from smtpd import MailmanProxy


qtde_linhas = int(input('Digite a quantidade de linhas: '))
qtde_col = int(input('Digite a quantidade de colunas: '))

matriz = [[None]*qtde_col for i in range(qtde_linhas)]

for linha in range(qtde_linhas):
    for coluna in range(qtde_col):
        matriz[linha][coluna] = randint(1,20)

for linha in range(qtde_linhas):
    for coluna in range(qtde_col):
        print(f'{matriz[linha][coluna]:4}',end='')
    print()

maior = matriz[0][0]

for linha in range(qtde_linhas):
    for coluna in range(qtde_col):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]

cont = 0
for linha in range(qtde_linhas):
    for coluna in range(qtde_col):
        if maior == matriz[linha][coluna]:
            cont+=1
            print(f'{linha}x{coluna}')
            