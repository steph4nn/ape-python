file = open('CADASTRO.TXT', 'r')
macho = open('macho.txt', 'w')
femea = open('femea.txt', 'w')
list = file.readlines()

for i in range(len(list)):
    linha = list[i]
    linha = linha.split(',')
    if linha[1] == 'M':
        macho.write(f'{linha[0]}' +'\n')
    else:
        femea.write(f'{linha[0]}' +'\n')
    print(linha)