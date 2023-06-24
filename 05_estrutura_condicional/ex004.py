nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: ').upper()

if (sexo =='M' or sexo =='MASCULINO'):
    print(f'Olá, Senhor {nome}')
else:
    print(f'Olá, Senhora {nome}')