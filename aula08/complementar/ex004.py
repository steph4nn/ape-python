massa = float(input('Digite a quantidade de gramas: '))
cont = 50


while massa >= 0.5:
    massa = massa/2
    cont+= 50
print(f'Foram necessários {cont} segundos para a massa se tornar menor que 0.5g')