file_1 = open('teste.txt', 'r')
conteudo_1 = file_1.read()
file_2 =  open('teste2.txt', 'r')
conteudo_2 = file_2.read()
file_3 = open('conca.txt', 'a')

file_3.write(conteudo_1)
file_3.write(conteudo_2)



file_1.close()
file_2.close()
file_3.close()