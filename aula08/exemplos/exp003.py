n = int(input('Digite uma quantidade de números: '))
cont = 1
while cont <= n:
    valor = int(input('Digite um número:'))
    if valor %2 == 0:
        print(f'O número {valor} é par!')
    else:
        print(f'O número {valor} é impar!')
