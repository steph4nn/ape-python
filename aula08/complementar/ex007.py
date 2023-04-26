ano = 2023

FLAG = 'NAO'
resposta = ''

while resposta != FLAG:
    
    nome = input('Digite seu nome: ')
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    ano_ingresso = int(input('Digite o ano em que entrou na empresa: '))

    idade = ano - ano_nasc
    tempo_trab = ano - ano_ingresso
    
    print(f'O colaborador {nome}, tem {idade} anos e atua na empresa há {tempo_trab}')

    if idade >= 65 or tempo_trab >= 30 or idade >= 60 and tempo_trab >= 25:
        print('Tem direito a aposentadoria')
    else:
        print('Não tem direito a aposentadoria')
    resposta = input('Você deseja repetir o processo? ').upper()
    