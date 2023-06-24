N = int(input('Digite a quantidade de números a serem lidos: '))
V = [None]*N

menor_num = 9999999
maior_num = -999999999
ind_menor = 999999
ind_maior = -999

for i in range(N):
    V[i] = int(input('Digite um número: '))
    if V[i] < menor_num:
        menor_num = V[i]
        ind_menor = i
    if V[i] > maior_num:
        maior_num = V[i]
        ind_maior = i
print(f'O menor número do vetor é {menor_num} de indice {ind_menor}, o maior num do vetor é {maior_num} de indice {ind_maior}')