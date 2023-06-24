valor1 = float(input('digite um valor: '))
valor2 = float(input('digite outro valor: '))

operador = input('Selecione o operador: ').lower()


match operador:
    case '+':
        print(f'{valor1 + valor2}')
    case '-':
        print(f'{valor1-valor2}')
    case 'x' | '*':
        print(f'{valor1*valor2}')
    case'/':
        if valor2 !=0:
            print(f'{valor1/valor2}')
        else:
            print('Não é possivel dividir por 0!')
    case '%':
        if valor2 !=0:    
            print(f'{valor1%valor2}')
        else:
            print('Não é possivel dividir por 0!')
    case _:
        print('Opção inválida')