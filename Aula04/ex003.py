#equilatero 3 lados iguals
#isosceles 2 lados iguais 1 diff
#escaleno todos diferentes

ladoa = int(input('Digite o valor do lado A: '))
ladob = int(input('Digite o valor do lado B: '))
ladoc = int(input('Digite o valor do lado C: '))

if (ladoa, ladob, ladoc <= 0):
    print('Digite um valor válido!')
elif (ladoa == ladob == ladoc):
    print('Trata-se de um triângulo Equilátero.')
elif (ladoa == ladob or ladoc==ladoa or ladob==ladoc):
    print('Trata-se de um triângulo Isósceles.')
elif (ladoa != ladob != ladoc):
    print('Trata-se de um triângulo escaleno')



print('FIMTESTE')