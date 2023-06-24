V = [None]*3
K = int(input('Digite o valor a ser encontrado: '))
cont = 0

for i in range(3):
    V[i] = int(input('Digite um número: '))

print(f'{V.count(K)}')

