for i in range(30):
    temp = float(input('Digite a temperatura: '))
    if i == 0:
        menor_temp = temp
        maior_temp = temp
    if temp > maior_temp:
        maior_temp = temp
    if temp < menor_temp:
        menor_temp = temp
print(f'A maior temperature foi {maior_temp} graus e a menor foi {menor_temp} graus.')
