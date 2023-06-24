# lista = [1 ,2 ,3, 4, 5]
# print(lista[::-1])

N = int(input('Digite a quantidade de números: '))
V = [None]*N

for i in range(N):
    V[i] = int(input('Digite um número: '))

print(f'Os valores do vetor V são {V}')
print(f'Os valores do vetor V invertidos são {V[::-1]}')