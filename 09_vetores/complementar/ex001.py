N = int(input('Digite a quantidade de num: '))                                                  
vetor = [None]*N
pares = impar = 0


for index in range(N):
    vetor[index] = int(input('Digite um num: '))

for index in range(N):
    if vetor[index]%2==0:
        pares+= 1
for index in range(N):
    if vetor[index]%2!=0:
        impar += 1
soma = sum(vetor)
media = soma/N

print(f'qtde de pares: {pares}; qtde de impares: {impar}; soma de tds: {soma}; media: {media}')
