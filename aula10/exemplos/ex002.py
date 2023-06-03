nlin = int(input('Num de linhas: '))
ncol = int(input('Num de col: '))

m = [[None]*ncol for i in range(nlin)]

print('Entre com os elementos da matriz')

for i in range(nlin):
    for j in range(ncol):
        m[i][j] = int(input(f'{i}x{j}: '))

s = 0

for i in range(nlin):
    for j in range(ncol):
        s += m[i][j]

print(f'A soma de todos os elementos da matriz deu {s}')