num = int(input('Digite um valor: '))
print('''Selecione uma opção:
    BINARIO
    DECIMAL
    HEXADECIMAL
    : ''')
opcao = input('Digite sua opção: ').upper()

if opcao == 'BINARIO':
    print(f'{bin(num)[2::]}')
elif opcao == 'DECIMAL':
    print(f'{int(num)}')
elif opcao == 'HEXADECIMAL':
    print(f'{hex(num)[2::]}')
else:
    print('Escolha uma opção válida.')