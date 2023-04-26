for i in range(1,31):
    temp = float(input('Digite a temperatura: '))
    if i == 0:
        menor_temp = temp
        maior_temp = temp
        dia_quente = 0
        dia_frio = 0
    if temp > maior_temp:
        maior_temp = temp
        dia_quente = i
    if temp < menor_temp:
        menor_temp = temp
        dia_frio = i
print(f'A maior temperature foi no dia {dia_quente} c {maior_temp} graus e a menor foi no dia {dia_frio} c {menor_temp} graus.')
