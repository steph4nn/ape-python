vetor = []
print('Gerando o vetor')
for i in range(6):
    vetor.append(int(input('Digite um num: ')))
for index in range(6):
    if vetor.count(vetor[index]) == 1:
         print(f'{vetor[index]} não possui repetições dentro do vetor')
    else:
        print(f'{vetor[index]} possui repetições dentro do vetor')
   