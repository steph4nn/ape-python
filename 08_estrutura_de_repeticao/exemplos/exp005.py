n = int(input('Digite um valor: '))
cont = 0
while n!=0 | cont <= 100:
    cont += n
    if cont <= 100:
        print(f'A soma dos números deu: {cont}')
        n = int(input('Digite outro valor: '))
    else:
        print('A soma dos valores foi superior a 100!')
print('fim!')
print(f'A soma dos valores obtidos foi: {cont}')