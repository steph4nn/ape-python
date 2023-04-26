FLAG = 0
cont = 0
maisnovo = 999999
jovens= 0
idade =1 
somaidade = 0

while idade != FLAG:
    idade = int(input('Informe sua idade: '))
    somaidade += idade
    cont += 1
    media = somaidade/cont
    if idade >= 18 and idade <=21:
        jovens += 1
    if idade <= maisnovo:
        maisnovo = idade
    mediajovem = (jovens/cont)*100
print(f'A média de idade do público é: {media}')
print(f'A porcentagem de pessoas com idade entre 18 e 21 anos é: {mediajovem:.2f}%')
print(f'A idade do visitante mais novo foi: {maisnovo}')
