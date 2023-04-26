matricula = int(input('Digite o seu número de matrícula: '))

while matricula != 0:
    matricula = int(input('Digite o seu número de matrícula: '))
    nome = input('Digite seu nome: ')
    nota_um = int(input('Informe sua primeira nota: '))
    nota_dois = int(input('Informe sua segunda nota: '))
    media = (nota_um+nota_dois)/2
    if media >= 7:
        print(f'Matricula: {matricula}, nome: {nome}, media: {media}, você foi aprovado!')
    else:
        print(f'Matricula: {matricula}, nome: {nome}, media: {media}, você foi reprovado!')
    matricula = int(input('Digite o seu número de matrícula: '))


