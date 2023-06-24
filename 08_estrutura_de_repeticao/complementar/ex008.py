equipe_a = 0
equipe_b = 0

while equipe_a < 5 and equipe_b < 5:
    ponto = input('Qual equipe pontuou? ').upper()
    if ponto == 'A':
        equipe_a += 1
    if ponto == 'B':
        equipe_b += 1
    if ponto != 'A' and ponto != 'B':
        print('Digite uma equipe válida!')
if equipe_a - equipe_b >= 2:
    print(f'A equipe A venceu por {equipe_a}x{equipe_b}')
elif equipe_b - equipe_a >= 2:
    print(f'A equipe B venceu por {equipe_b}x{equipe_a}')
else: 
    print('A partida só acaba com uma diferença de dois pontos')
