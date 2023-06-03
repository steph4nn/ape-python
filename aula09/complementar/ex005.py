num_sort = [6 ,7 ,13, 14, 26]
apostadores = 2
dezenas = [None]*8
cont_dez = 0

for index in range(apostadores):
    print(f'Apostador num {index+1}. ')
    for k in range(8):
        num = int(input('Aposte um núm: '))
        if num >=1 and num <=80:
            dezenas[k] = num
        else:
            print('Escolha um número no intervalo válido!')
        if num_sort.count(num) == 1:
                cont_dez+=1
    print(f'Apostador num {index+1} acertou um total de {cont_dez} números da aposta!')

            
