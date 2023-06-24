nome = input('Digite seu nome: ')
SALARIO_B = 1000
carros_qtde = int(input('Digite a quantidade de carros vendidos: '))
COMISSAO = 200*carros_qtde
valor_venda = float(input('Digite o valor total das vendas: '))
PORCENTAGEM = 0.05*valor_venda
SALARIO_F = SALARIO_B+COMISSAO+PORCENTAGEM
print(f'O vendedor {nome} vendeu {carros_qtde} carros e o seu salário foi R${SALARIO_F:.2f}')

