N = [None]*10

for i in range(10):
    N[i] = int(input('Digite um número: '))

for i in range(0,10,2):
        print(f'Esses são os números com indice par: {N[i]}')
for i in range(1,10,2):
        print(f'Esses são os números com indice impar: {N[i]}')
