N = int(input('Digite a quantidade de números: ')) 
V = [None]*N
K = int(input('Digite o valor a ser encontrado: '))

for i in range(N):
    V[i] = int(input('Digite um número: '))
    if K == V[i]:
        print(i)