km_antes = float(input('Digite quantos Km tinha rodado antes da viagem: '))
km_depois = float(input('Digite quantos Km ficaram marcado depois da viagem: '))
KMRODADO = km_depois-km_antes

gasolina_gasta = float(input('Digite quantos litros de gasolina foram gastos: '))
gasolina_preço = float(input('Digite o valor da gasolina: '))
km_litro = KMRODADO/gasolina_gasta
tank = float(input('Digite a capacidade do tanque de combustivel: '))

CUSTO = km_litro*gasolina_preço
AUTONOMIA = (km_litro*tank)




input(f'Você percorreu {KMRODADO} km, o carro fez {km_litro:.2f}Km/l rodado, com o tank cheio você consegue rodar {AUTONOMIA:.2f} km, o custo da viagem foi R${CUSTO:.2f}')

