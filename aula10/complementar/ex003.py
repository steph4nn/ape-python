from random import randint


ORDEM = 3

matriz = [[None]*ORDEM for i in range(ORDEM)]

for linha in range(ORDEM):
    for coluna in range(ORDEM):
        matriz[linha][coluna] = randint(1,100)

print('A matriz foi gerada: ')
for linha in range(ORDEM):
    for coluna in range(ORDEM):
        print(f'{matriz[linha][coluna]:4}', end='')
    print('')

#SOMA DAS LINHAS
for linha in range(ORDEM):
    soma_linha = 0
    soma_linha += sum(matriz[linha])
    print(f'A soma dos valores da {linha+1}° linha foi: {soma_linha}')


#SOMA DE CADA COLUNA
for coluna in range(ORDEM):
    soma_coluna = 0
    for linha in range(ORDEM):
        soma_coluna += matriz[linha][coluna]
    print(f'A soma dos valores da {coluna+1}º coluna foi: {soma_coluna}')


#SOMA DOS ELEMENTOS DA DIAGONAL PRINCIPAL
soma_principal = 0
for k in range(ORDEM):
    soma_principal += matriz[k][k]
print(f'A soma da diagonal principal foi: {soma_principal}')


#SOMA DOS ELEMENTOS DA DIAGONAL SECUNDÁRIA
soma_secundaria = 0
for linha in range(ORDEM):
    for coluna in range(ORDEM):
        if linha + coluna == ORDEM-1:
            soma_secundaria += matriz[linha][coluna]
print(f'A soma dos elementos da diagonal secundária foi: {soma_secundaria}')


#SOMA DE TODOS OS ELEMENTOS
soma_geral = 0
for linha in range(ORDEM):
    for coluna in range(ORDEM):
        soma_geral += matriz[linha][coluna]
print(f'A soma de todos os elementos da matriz foi: {soma_geral}')