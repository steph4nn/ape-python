altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso: '))
IMC = peso/(altura*altura)



if (IMC>39.9):
    print('caixão')
elif (IMC>=35 and IMC<= 39.9):
    print('Você está com Obesidade grau II')
elif (IMC>=30):
    print('Você está com Obesidade grau I')
elif (IMC>=25):
    print('Você está com sobrepeso')
elif (IMC>=18.5):
    print('Você está com o peso normal')
else: 
    print('Você está abaixo do peso')
