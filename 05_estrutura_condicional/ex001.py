num_inicial = float(input('Digite um valor: '))
num_final = num_inicial%2

if (num_final==0):
    print(f'{num_inicial:.0f} é um valor par')
else:
    print(f'{num_inicial:.0f} é um valor impar')