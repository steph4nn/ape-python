cond = 'naosei'

while cond != 'SIM':
    num = int(input('Digite um número: '))
    par = num%2
    if par == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é impar!')
    cond = input('Você deseja sair do programa? ').upper()
