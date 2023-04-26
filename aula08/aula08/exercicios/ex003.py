maior = -99999999
menor = 99999999
cont = 0
while cont <= 5:
    num = int(input('Digite um número: '))
    cont +=1
    if num !=0:
        if num >= maior:
            maior = num
        if num <= menor:
            menor = num
    else:
        print('Digite um número válido!')
print(f'O maior número digitado foi {maior} e o menor número foi {menor}!')
    