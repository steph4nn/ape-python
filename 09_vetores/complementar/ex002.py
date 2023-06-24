N = int(input('Digite a qtde de num: '))
A = [None]*N
B = [None]*N
C = []

for index in range(N):
    A[index] = int(input('Digite um num: '))
    B[index] = int(input('Digite outro num: '))

for index in range(N):
    C.append(A[index])
    C.append(B[index])

print(f'Primeira lista: {A}; Segunda lista: {B}; Intercalação das duas: {C}')
 
