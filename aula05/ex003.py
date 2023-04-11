valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
valor3 = int(input('Digite mais um número: '))

if (valor1 > valor2 and valor1 > valor3):
    print(f'{valor1}')
elif (valor2 > valor1 and valor2 > valor3):
    print(f'{valor2}')
else:
    print(f'{valor3}')


print('FIMTESTE')