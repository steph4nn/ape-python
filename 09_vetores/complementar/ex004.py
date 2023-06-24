from ast import Num


vetor = []
print('Gerando o vetor')
for i in range(6):
    num = int(input('Digite um num: '))
    if vetor.count(num) == 0:
       vetor.append(num)
    else:
        print('Esse número ja está na lista.')
print(vetor)
