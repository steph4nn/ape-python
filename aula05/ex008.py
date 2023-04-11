valor1 = float(input('digite um valor: '))
valor2 = float(input('digite outro valor: '))

operador = input('Selecione o operador: ').lower()

if operador == '+':
    print(f'{valor1 + valor2}')
elif operador == '-':
    print(f'{valor1-valor2}')
elif operador == 'x':
    print(f'{valor1*valor2}')
elif operador == '/':
    if valor2 !=0:
        print(f'{valor1/valor2}')
    else:
        print('Não é possivel dividir por 0!')
elif operador == '%':
    if valor2 !=0:    
        print(f'{valor1%valor2}')
    else:
        print('Não é possivel dividir por 0!')
else:
    print('Opção inválida')