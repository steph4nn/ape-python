file = open('CADASTRO.TXT', 'r')
list = file.readlines()
print(list)

sum_m = 0
sum_f= 0
cont_m=0
cont_f=0
for i in range(len(list)):
    linha = list[i]
    linha = linha.split(',')
    sexo = linha [1].upper()
    if sexo == 'M':
        idade = linha[:3][2]
        sum_m+=int(idade)
        cont_m+=1
    else:
        idade = linha[:3][2]
        sum_f+=int(idade)
        cont_f+=1
    print(idade)

print((sum_m/cont_m), (sum_f/cont_f))