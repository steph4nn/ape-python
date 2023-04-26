valor = int(input('Digite um valor: '))
cont = 0

while valor !=0:
    print(f'O dobro de {valor} é {valor*2}')
    valor = int(input('Digite outro valor: '))
    cont += 1
else:
    print('Fim!')
print(f'Foram lidos {cont} números!')