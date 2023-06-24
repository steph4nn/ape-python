import os

nome = input()
file = f"./aula14/ex01/nom{nome}.txt"

print(file)
if os.path.exists(file):
    
    arquivo = open(file, 'r')
    print(arquivo.read())
    arquivo.close()
