cont = 0
soma = 0

while cont <= 5:
    num = int(input('Digite um número: '))
    cont +=1
    soma += num
    media = soma/cont
    print(f'a média dos números digitados até o momento é: {media}')
