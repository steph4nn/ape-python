from random import randint

N = int(input('Digite a ordem da Matriz: '))
ORDEM = N

matriz = [[None]*ORDEM for i in range(ORDEM)]

for linha in range(ORDEM):
    for coluna in range(ORDEM):
        matriz[linha][coluna] = int(input(f'Digite o número {linha}x{coluna}: '))

print('Matriz gerada: ')
for linha in range(ORDEM):
    for coluna in range(ORDEM):
        print(f'{matriz[linha][coluna]:4}',end='')
    print('')

magic = True
somat = sum(matriz[0]) #valor base da soma magica-

for linha in range(ORDEM):
    soma_linha = sum(matriz[linha])
    if somat != soma_linha:
        magic = False
        print('Não é um quadrado mágico!')
        break

if magic:
    for coluna in range(ORDEM):
            soma_coluna = 0
            for linha in range(ORDEM):
                soma_coluna+= matriz[linha][coluna]
    if soma_coluna != somat:
                magic = False
                print('Não é um quadrado mágico, a soma das colunas não bate!')
                
if magic: 
    soma_principal = 0
    for k in range(ORDEM):
        soma_principal += matriz[k][k]
    if soma_principal !=somat:
        magic = False
        print('Não é um quadrado mágico, a soma da diagonal principal não bate!')
            

if magic:
    soma_secundaria = 0
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            if coluna + linha == ORDEM -1:
                soma_secundaria += matriz[linha][coluna]
    if soma_secundaria != somat:
        magic = False
        print('A soma da diagonal secundária não bateu!')

if magic:
    print('É um quadrado mágico!!')
else:
    print('Tente novamente')
