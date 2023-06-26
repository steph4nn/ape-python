file = open('teste.txt', 'r')
list =file.readlines()
# i = 0
# for palavra in list:
#     print(f'{i+1} {palavra}')
#     i += 1
for linha in list:
    print(linha, end='')
file.close()