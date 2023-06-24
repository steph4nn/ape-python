SALARIO_MINIMO = 1300
VENDAS = float(input('Digite o valor vendido no mês: '))
COMISSAO =0.05*VENDAS

if COMISSAO < SALARIO_MINIMO:
    print(f'Seu salário vai ser R${SALARIO_MINIMO:.2F}')
else:
    print(f'Seu salário vai ser R${COMISSAO:.2F}')
