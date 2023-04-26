senha = 'abcd'
tentativa = input('Digite a senha: ')

while senha != tentativa:
    for i in range(2):
        tentativa = input(f'Tente novamente, você ainda tem {2-i} chances: ')
    else:
        print('Acesso negado!')
        break
print('Tente novamente mais tarde.')
