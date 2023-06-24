N = int(input('Digite a ordem da matriz: '))
LINHAS = COLUNAS = N

matriz = [[None]*COLUNAS for i in range(LINHAS)]

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz[linha][coluna] = int(input('Digite um valor: '))

print('Matriz gerada: ')

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{matriz[linha][coluna]:4}',end='')
    print('')

permut = True

for linha in range(LINHAS):
    if sum(matriz[linha]) > 1:
        permut = False
        break


if permut:
    for coluna in range(COLUNAS):
        soma = 0
        for linha in range(LINHAS):
            soma += matriz[linha][coluna]
            if soma > 1:
                permut = False
print(permut)