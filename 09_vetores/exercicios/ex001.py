N = int(input('Digite a quantidade de números: '))
A = [None]*N
K = int(input('Digite o multiplicador: '))

B = [None]*N
for i in range(N):
    A[i] = int(input('Digite um número: '))
for i in range(N):
    B[i] = A[i]*K
print(B)