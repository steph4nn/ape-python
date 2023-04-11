nome = input('Digite seu nome: ')
conceito = input('Digite seu conceito: ').upper()

if conceito == 'A':
    print(f'{nome}, Fortemente recomendado!')
elif conceito == 'B' or conceito == 'C':
    print(f'{nome}, Recomendado.')
else: 
    print(f'{nome}, não recomendado.')
